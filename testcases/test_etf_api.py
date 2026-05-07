# -*- coding: utf-8 -*-
"""ETF 模块接口用例。

正常用例覆盖：分页列表、统计 type=1/2、相关推荐 type=1/2。
异常用例覆盖：参数类型错误、边界值（基于实测响应）。
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


pytestmark = [allure.epic("ETF模块")]


ETF_PAGE_PATH = "/xhj-gather-app/open/etf/page"
ETF_STATISTICS_PATH = "/xhj-gather-app/open/etf/statistics"
ETF_SEARCH_RELATED_PATH = "/xhj-gather-app/open/etf/searchRelated"


def _assert_etf_response_basic(res):
    """复用公共断言并补充 ETF 通用结构校验：HTTP 200 + 合法 JSON + 主体含 data。"""
    assert_http_ok(res)
    body = assert_json_response(res)
    assert isinstance(body, dict), (
        "ETF接口响应主体类型错误，期望 dict。\n"
        f"{response_detail(res)}"
    )
    assert "data" in body, (
        "ETF接口响应缺少 data 字段。\n"
        f"响应字段: {list(body.keys())}\n"
        f"{response_detail(res)}"
    )
    return body


# ────────────────────────── 正常用例 ──────────────────────────


@allure.feature("ETF分页")
@allure.story("正常查询")
@allure.title("ETF分页列表接口")
@allure.description("请求 App 实际使用的 ETF 分页列表接口，校验 HTTP 状态码、JSON 解析和基础响应结构。")
def test_etf_page(client):
    with allure.step("发送请求"):
        res = client.get(
            ETF_PAGE_PATH,
            params={"asc": 0, "limit": 20, "locale": "us", "page": 1},
        )

    with allure.step("断言 HTTP/JSON/主体结构"):
        _assert_etf_response_basic(res)


@allure.feature("ETF统计")
@allure.story("正常查询-type=1")
@allure.title("ETF统计接口-type=1")
def test_etf_statistics_type_1(client):
    with allure.step("发送请求"):
        res = client.get(ETF_STATISTICS_PATH, params={"locale": "us", "type": 1})

    with allure.step("断言 HTTP/JSON/主体结构"):
        _assert_etf_response_basic(res)


@allure.feature("ETF统计")
@allure.story("正常查询-type=2")
@allure.title("ETF统计接口-type=2")
def test_etf_statistics_type_2(client):
    with allure.step("发送请求"):
        res = client.get(ETF_STATISTICS_PATH, params={"locale": "us", "type": 2})

    with allure.step("断言 HTTP/JSON/主体结构"):
        _assert_etf_response_basic(res)


@allure.feature("ETF相关推荐")
@allure.story("正常查询-type=1")
@allure.title("ETF相关推荐接口-type=1")
def test_etf_search_related_type_1(client):
    with allure.step("发送请求"):
        res = client.get(ETF_SEARCH_RELATED_PATH, params={"type": 1})

    with allure.step("断言 HTTP/JSON/主体结构"):
        _assert_etf_response_basic(res)


@allure.feature("ETF相关推荐")
@allure.story("正常查询-type=2")
@allure.title("ETF相关推荐接口-type=2")
def test_etf_search_related_type_2(client):
    with allure.step("发送请求"):
        res = client.get(ETF_SEARCH_RELATED_PATH, params={"type": 2})

    with allure.step("断言 HTTP/JSON/主体结构"):
        _assert_etf_response_basic(res)


# ────────────────────────── 异常用例：边界值 ──────────────────────────


@allure.feature("ETF分页")
@allure.story("边界值")
@pytest.mark.parametrize(
    "params, case_name",
    [
        ({"asc": 0, "limit": 0, "locale": "us", "page": 0}, "page=0且limit=0"),
        ({"asc": 0, "limit": 1, "locale": "us", "page": 1}, "limit=1"),
        ({"asc": 0, "limit": 100, "locale": "us", "page": 1}, "limit=100"),
    ],
    ids=["page=0且limit=0", "limit=1", "limit=100"],
)
def test_etf_page_boundary(client, params, case_name):
    """实测：服务端对边界分页参数兼容处理，仍返回 code=200。"""
    allure.dynamic.title(f"ETF分页 - 边界值 - {case_name}")

    with allure.step(f"发送边界值请求：{case_name}"):
        res = client.get(ETF_PAGE_PATH, params=params)

    with allure.step("断言响应基础结构"):
        assert_http_ok(res)
        body = assert_business_success(res)
        assert isinstance(body.get("data"), dict), (
            f"边界值 {case_name} 下 data 期望 dict。\n"
            f"{response_detail(res)}"
        )


# ────────────────────────── 异常用例：参数类型错误 ──────────────────────────


@allure.feature("ETF分页")
@allure.story("参数类型错误")
@pytest.mark.parametrize(
    "params, case_name",
    [
        ({"asc": 0, "limit": "abc", "locale": "us", "page": 1}, "limit类型错误"),
    ],
    ids=["limit类型错误"],
)
def test_etf_page_invalid_param(client, params, case_name):
    """实测：limit=abc 时返回 code=500, msg=服务繁忙。"""
    allure.dynamic.title(f"ETF分页 - 参数异常 - {case_name}")

    with allure.step(f"发送异常请求：{case_name}"):
        res = client.get(ETF_PAGE_PATH, params=params)

    with allure.step("断言异常响应：code 不为 200"):
        body = assert_error_response(res)
        assert body.get("code") != 200, (
            f"参数异常 {case_name} 下业务 code 不应为 200。\n"
            f"{response_detail(res)}"
        )


@allure.feature("ETF统计")
@allure.story("参数类型错误")
@pytest.mark.parametrize(
    "params, case_name",
    [
        ({"locale": "us", "type": "abc"}, "type类型错误"),
    ],
    ids=["type类型错误"],
)
def test_etf_statistics_invalid_param(client, params, case_name):
    """实测：type=abc 时返回 code=500。"""
    allure.dynamic.title(f"ETF统计 - 参数异常 - {case_name}")

    with allure.step(f"发送异常请求：{case_name}"):
        res = client.get(ETF_STATISTICS_PATH, params=params)

    with allure.step("断言异常响应：code 不为 200"):
        body = assert_error_response(res)
        assert body.get("code") != 200, (
            f"参数异常 {case_name} 下业务 code 不应为 200。\n"
            f"{response_detail(res)}"
        )
