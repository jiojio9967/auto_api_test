# -*- coding: utf-8 -*-
"""IM 群组模块接口用例。

包含正常用例（搬运自原 test_auto_api.py 的 IM 用例）和参数化异常用例。
异常用例的断言基于 Charles + 实测响应，不强行要求 code=200。
"""
import allure
import pytest
import requests

from public.assertions import (
    assert_business_success,
    assert_error_response,
    assert_field_type,
    assert_has_keys,
    assert_http_ok,
    assert_json_response,
    response_detail,
)
from public.config import BASE_URL
from public.headers import get_headers


pytestmark = [allure.epic("IM群组模块")]


IM_GROUP_ID = 15
BANNER_V2_PATH = "/xhj-gather-app/im/group/bannerV2"
BANNER_PATH = "/xhj-gather-app/im/group/banner"


# ────────────────────────── 正常用例 ──────────────────────────


@allure.feature("群组Banner")
@allure.story("正常查询")
@allure.title("IM 群组 Banner 接口")
def test_im_group_banner(client):
    with allure.step("发送 IM 群组 Banner 请求"):
        res = client.get(BANNER_PATH, params={"groupId": IM_GROUP_ID})

    with allure.step("断言 HTTP 状态码"):
        assert_http_ok(res)

    with allure.step("断言响应基础结构"):
        body = assert_business_success(res)
        assert isinstance(body.get("data"), dict), (
            "IM 群组 Banner 接口 data 类型错误，期望 dict。\n"
            f"{response_detail(res)}"
        )


@allure.feature("群组Banner")
@allure.story("正常查询")
@allure.title("IM 群组 Banner V2 接口")
@allure.description("Banner V2 接口正常请求需要携带 groupId，校验广告位/话题/机器人指令结构。")
def test_im_group_banner_v2(client):
    with allure.step("发送 IM 群组 Banner V2 请求"):
        res = client.get(BANNER_V2_PATH, params={"groupId": IM_GROUP_ID})

    with allure.step("断言 HTTP 状态码"):
        assert_http_ok(res)

    with allure.step("断言响应主结构"):
        body = assert_business_success(res)
        assert isinstance(body.get("data"), dict), (
            "IM 群组 Banner V2 接口 data 类型错误，期望 dict。\n"
            f"{response_detail(res)}"
        )

    with allure.step("断言 Banner V2 数据结构"):
        data = body["data"]
        banner_key = "adws" if "adws" in data else "advs"
        assert banner_key in data and isinstance(data[banner_key], list), (
            "IM 群组 Banner V2 接口 data.adws/advs 缺失或类型错误，期望 list。\n"
            f"{response_detail(res)}"
        )
        assert_field_type(data, "topics", list, "data", res)
        assert_field_type(data, "robotInstruct", list, "data", res)

    with allure.step("如果机器人指令不为空，断言第一条指令字段"):
        if data["robotInstruct"]:
            first_item = data["robotInstruct"][0]
            assert isinstance(first_item, dict), (
                "IM 群组 Banner V2 接口 robotInstruct 第一条数据类型错误，期望 dict。\n"
                f"{response_detail(res)}"
            )
            for field in ("tip", "instruct", "text"):
                assert_field_type(first_item, field, str, "robotInstruct[0]", res)


@allure.feature("群组推荐")
@allure.story("正常查询")
@allure.title("IM 群组推荐接口")
def test_im_group_recommend(client):
    res = client.get("/xhj-gather-app/im/group/recommend", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("我的群组")
@allure.story("正常查询")
@allure.title("我的 IM 群组列表接口")
def test_im_group_mine(client):
    with allure.step("发送我的 IM 群组列表请求（带分页参数）"):
        res = client.get(
            "/xhj-gather-app/im/group/mine",
            params={"page": 1, "limit": 10},
        )

    with allure.step("断言 HTTP 状态码与业务 code"):
        assert_http_ok(res)
        body = assert_business_success(res)

    with allure.step("断言分页结构 totalCount/pageSize/totalPage/currPage/list"):
        data = body["data"]
        assert isinstance(data, dict), (
            "我的 IM 群组列表 data 类型错误，期望 dict。\n"
            f"{response_detail(res)}"
        )
        assert_field_type(data, "totalCount", int, "data", res)
        assert_field_type(data, "pageSize", int, "data", res)
        assert_field_type(data, "totalPage", int, "data", res)
        assert_field_type(data, "currPage", int, "data", res)
        assert_field_type(data, "list", list, "data", res)
        assert data["currPage"] == 1, (
            "我的 IM 群组列表 data.currPage 应等于请求 page=1。\n"
            f"{response_detail(res)}"
        )


@allure.feature("群组公告")
@allure.story("正常查询")
@allure.title("最新群公告接口")
def test_im_group_notice_last(client):
    res = client.get("/xhj-gather-app/im/groupNotice/last")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 异常用例：参数 ──────────────────────────


@allure.feature("群组Banner")
@allure.story("缺少必填参数")
@pytest.mark.parametrize(
    "params, case_name",
    [
        ({}, "缺少groupId"),
        ({"groupId": ""}, "groupId为空"),
        ({"groupId": "abc"}, "groupId类型错误"),
    ],
    ids=["缺少groupId", "groupId为空", "groupId类型错误"],
)
def test_im_group_banner_v2_invalid_param(client, params, case_name):
    """实测：异常参数下接口返回 code=500，msg='服务繁忙，请稍后再试'，data is None。"""
    allure.dynamic.title(f"群组Banner V2 - 参数异常 - {case_name}")

    with allure.step(f"发送异常请求：{case_name}"):
        res = client.get(BANNER_V2_PATH, params=params)

    with allure.step("断言已知服务端500场景：code=500 + msg含'服务繁忙' + data is None"):
        assert_error_response(
            res,
            expected_codes=(500,),
            expected_msg_keywords=("服务繁忙",),
            expect_data_none=True,
        )


@allure.feature("群组Banner")
@allure.story("边界值")
@pytest.mark.parametrize(
    "group_id, case_name",
    [
        (-1, "groupId为负数"),
        (99999999, "groupId为不存在ID"),
    ],
    ids=["groupId为负数", "groupId为不存在ID"],
)
def test_im_group_banner_v2_boundary_group_id(client, group_id, case_name):
    """边界值实测：服务端返回 code=200 但 data 为空 dict。"""
    allure.dynamic.title(f"群组Banner V2 - 边界值 - {case_name}")

    with allure.step(f"发送边界值请求：{case_name}"):
        res = client.get(BANNER_V2_PATH, params={"groupId": group_id})

    with allure.step("断言响应可解析"):
        assert_http_ok(res)
        body = assert_json_response(res)

    with allure.step("断言业务 code 与 data 结构"):
        assert body.get("code") == 200, (
            f"边界值 {case_name} 下业务 code 应为 200。\n"
            f"{response_detail(res)}"
        )
        assert isinstance(body.get("data"), dict), (
            f"边界值 {case_name} 下 data 期望 dict。\n"
            f"{response_detail(res)}"
        )


# ────────────────────────── 异常用例：未登录 ──────────────────────────


def _build_headers(auth_value):
    headers = dict(get_headers())
    if auth_value is None:
        headers.pop("authorization", None)
    else:
        headers["authorization"] = auth_value
    return headers


@allure.feature("群组Banner")
@allure.story("未登录访问")
@pytest.mark.parametrize(
    "auth_value, case_name, expected_codes",
    [
        (None, "无Authorization头", (4011,)),
        ("", "Authorization为空", (4011,)),
        ("invalid_token_for_test", "Authorization为错误token", (4011, 4012)),
    ],
    ids=["无Authorization头", "Authorization为空", "Authorization为错误token"],
)
def test_im_group_banner_v2_unauthorized(base_url, auth_value, case_name, expected_codes):
    allure.dynamic.title(f"群组Banner V2 - 未登录 - {case_name}")
    headers = _build_headers(auth_value)

    with allure.step(f"使用 {case_name} 直接请求接口"):
        res = requests.get(
            f"{base_url}{BANNER_V2_PATH}",
            params={"groupId": IM_GROUP_ID},
            headers=headers,
            timeout=15,
        )

    with allure.step(f"断言未登录场景：code 命中 {expected_codes} + data is None"):
        assert_error_response(
            res,
            expected_codes=expected_codes,
            expect_data_none=True,
        )
