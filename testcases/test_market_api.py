# -*- coding: utf-8 -*-
"""行情/币种模块接口用例。

包含币种通知（大额提醒）、提醒分页、提醒记录等行情相关接口。
正常用例搬运自原 test_auto_api.py 的「币种通知」分组。
"""
import allure
import pytest

from public.assertions import (
    assert_business_success,
    assert_error_response,
    assert_http_ok,
    assert_json_response,
    response_detail,
)


pytestmark = [allure.epic("行情模块")]


CURRENCY_NOTICE_PAGE_PATH = "/xhj-gather-app/currencyNotice/page"


# ────────────────────────── 正常用例 ──────────────────────────


@allure.feature("大额提醒")
@allure.story("正常查询")
@allure.title("大额提醒状态-全币种")
def test_currency_notice_large_status_all(client):
    res = client.get("/xhj-gather-app/currencyNotice/largeStatusAll")
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("提醒分页")
@allure.story("正常查询")
@allure.title("提醒分页列表接口")
def test_currency_notice_page(client):
    res = client.get(CURRENCY_NOTICE_PAGE_PATH, params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("提醒分页")
@allure.story("正常查询")
@allure.title("提醒分页列表接口 V2")
def test_currency_notice_page_v2(client):
    res = client.get(
        "/xhj-gather-app/currencyNotice/pageV2",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("提醒记录")
@allure.story("正常查询")
@allure.title("提醒记录分页接口")
def test_currency_notice_record_page(client):
    res = client.get(
        "/xhj-gather-app/currencyNoticeRecord/page",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 异常用例：边界值 ──────────────────────────


@allure.feature("提醒分页")
@allure.story("边界值")
@pytest.mark.parametrize(
    "params, case_name",
    [
        ({"page": 0, "limit": 0}, "page=0且limit=0"),
        ({"page": 1, "limit": 1}, "limit=1"),
        ({"page": 1, "limit": 100}, "limit=100"),
    ],
)
def test_currency_notice_page_boundary(client, params, case_name):
    """实测：服务端对边界分页参数兼容处理，仍返回 code=200。"""
    allure.dynamic.title(f"提醒分页 - 边界值 - {case_name}")

    with allure.step(f"发送边界值请求：{case_name}"):
        res = client.get(CURRENCY_NOTICE_PAGE_PATH, params=params)

    with allure.step("断言响应基础结构"):
        assert_http_ok(res)
        body = assert_business_success(res)
        assert isinstance(body.get("data"), dict), (
            f"边界值 {case_name} 下 data 期望 dict。\n"
            f"{response_detail(res)}"
        )


# ────────────────────────── 异常用例：参数类型错误 ──────────────────────────


@allure.feature("提醒分页")
@allure.story("参数类型错误")
@pytest.mark.parametrize(
    "params, case_name",
    [
        ({"page": "abc", "limit": "abc"}, "page和limit均为字符串"),
    ],
)
def test_currency_notice_page_invalid_param(client, params, case_name):
    """实测：参数类型错误时接口返回 code=500。"""
    allure.dynamic.title(f"提醒分页 - 参数异常 - {case_name}")

    with allure.step(f"发送异常请求：{case_name}"):
        res = client.get(CURRENCY_NOTICE_PAGE_PATH, params=params)

    with allure.step("通用异常响应断言"):
        body = assert_error_response(res)

    with allure.step("断言业务 code 不为 200"):
        assert body.get("code") != 200, (
            f"参数异常 {case_name} 下业务 code 不应为 200。\n"
            f"{response_detail(res)}"
        )
