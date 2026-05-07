# -*- coding: utf-8 -*-
"""新币模块接口用例。

正常用例覆盖：新币分页列表（bjw-front 真实路径）。
异常用例覆盖：pageNum/pageSize 参数边界、类型错误（基于实测响应：服务端返回 code=500 + 具体校验信息）。
"""
import allure
import pytest

from public.assertions import (
    assert_error_response,
    assert_field_type,
    assert_http_ok,
    assert_json_response,
    response_detail,
)
from public.request import ApiClient


pytestmark = [allure.epic("新币模块")]


NEW_COINS_PATH = "/bjw-front/app/market/currency/v1/open/page/newCoins"
NEW_COINS_PARAMS = {
    "isAsc": 0,
    "orderByColumn": "launchTime",
    "pageNum": 1,
    "pageSize": 20,
    "period": "24h",
}


def _new_coins_attach(res):
    allure.attach(
        response_detail(res),
        name="newCoins 接口响应",
        attachment_type=allure.attachment_type.TEXT,
    )


# ────────────────────────── 正常用例 ──────────────────────────


@allure.feature("新币列表")
@allure.story("正常查询")
@allure.title("新币列表接口")
@allure.description(
    "请求 App 实际使用的新币分页列表接口，校验 HTTP 状态码、JSON 解析和 data.total/data.rows 基础结构。"
)
def test_new_coins(base_url, headers):
    with allure.step("创建接口客户端"):
        client = ApiClient(base_url, headers)

    with allure.step("请求新币分页列表接口"):
        res = client.get(NEW_COINS_PATH, params=NEW_COINS_PARAMS)
        _new_coins_attach(res)

    with allure.step("断言 HTTP 状态码为 200"):
        assert_http_ok(res)

    with allure.step("解析 JSON"):
        body = assert_json_response(res)

    with allure.step("断言响应结构"):
        assert isinstance(body, dict), (
            "新币列表接口响应主体类型错误，期望 dict。\n"
            f"{response_detail(res)}"
        )
        assert body.get("code") == 200, (
            "新币列表接口业务 code 异常，期望 200。\n"
            f"{response_detail(res)}"
        )
        assert "data" in body, (
            "新币列表接口响应缺少 data 字段。\n"
            f"{response_detail(res)}"
        )

        data = body["data"]
        assert isinstance(data, dict), (
            "新币列表接口 data 类型错误，期望 dict。\n"
            f"{response_detail(res)}"
        )
        assert_field_type(data, "total", int, "data", res)
        assert_field_type(data, "rows", list, "data", res)


# ────────────────────────── 异常用例：参数 ──────────────────────────


@allure.feature("新币列表")
@allure.story("参数边界值")
@pytest.mark.parametrize(
    "param_overrides, case_name",
    [
        ({"pageNum": 0}, "pageNum=0"),
        ({"pageSize": 0}, "pageSize=0"),
        ({"pageSize": 1000}, "pageSize=1000(超出最大值)"),
    ],
)
def test_new_coins_invalid_pagination(base_url, headers, param_overrides, case_name):
    """实测：服务端对参数有显式校验，返回 code=500 + 具体提示，例如：

    - pageNum=0   -> "pageNum必须大于等于1"
    - pageSize=0  -> "pageSize必须大于等于1"
    - pageSize=1000 -> "pageSize不能大于100"
    """
    allure.dynamic.title(f"新币列表 - 参数边界 - {case_name}")
    client = ApiClient(base_url, headers)
    params = {**NEW_COINS_PARAMS, **param_overrides}

    with allure.step(f"发送边界值请求：{case_name}"):
        res = client.get(NEW_COINS_PATH, params=params)
        _new_coins_attach(res)

    with allure.step("通用异常响应断言"):
        body = assert_error_response(res)

    with allure.step("断言业务 code 不为 200"):
        assert body.get("code") != 200, (
            f"参数边界 {case_name} 下业务 code 不应为 200。\n"
            f"{response_detail(res)}"
        )


@allure.feature("新币列表")
@allure.story("参数类型错误")
@pytest.mark.parametrize(
    "param_overrides, case_name",
    [
        ({"pageNum": "abc"}, "pageNum类型错误"),
        ({"pageSize": "abc"}, "pageSize类型错误"),
    ],
)
def test_new_coins_invalid_param_type(base_url, headers, param_overrides, case_name):
    """实测：参数类型错误返回 code=500，msg 包含 java 类型转换错误信息。"""
    allure.dynamic.title(f"新币列表 - 参数异常 - {case_name}")
    client = ApiClient(base_url, headers)
    params = {**NEW_COINS_PARAMS, **param_overrides}

    with allure.step(f"发送异常请求：{case_name}"):
        res = client.get(NEW_COINS_PATH, params=params)
        _new_coins_attach(res)

    with allure.step("通用异常响应断言"):
        body = assert_error_response(res)

    with allure.step("断言业务 code 不为 200"):
        assert body.get("code") != 200, (
            f"参数异常 {case_name} 下业务 code 不应为 200。\n"
            f"{response_detail(res)}"
        )
