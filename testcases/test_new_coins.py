# -*- coding: utf-8 -*-
import allure

from public.request import ApiClient


NEW_COINS_PATH = "/bjw-front/app/market/currency/v1/open/page/newCoins"
NEW_COINS_PARAMS = {
    "isAsc": 0,
    "orderByColumn": "launchTime",
    "pageNum": 1,
    "pageSize": 20,
    "period": "24h",
}


def _response_detail(res):
    return (
        f"请求URL  : {res.request.url}\n"
        f"HTTP状态 : {res.status_code}\n"
        f"响应内容 : {res.text}"
    )


@allure.title("新币列表接口")
@allure.description(
    "请求 App 实际使用的新币分页列表接口，校验 HTTP 状态码、JSON 解析和 data.total/data.rows 基础结构。"
)
def test_new_coins(base_url, headers):
    with allure.step("创建接口客户端"):
        client = ApiClient(base_url, headers)

    with allure.step("请求新币分页列表接口"):
        res = client.get(NEW_COINS_PATH, params=NEW_COINS_PARAMS)
        allure.attach(
            _response_detail(res),
            name="newCoins 接口响应",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("断言 HTTP 状态码为 200"):
        assert res.status_code == 200, (
            "新币列表接口 HTTP 状态码异常。\n"
            f"{_response_detail(res)}"
        )

    with allure.step("解析 JSON"):
        try:
            body = res.json()
        except ValueError as exc:
            raise AssertionError(
                "新币列表接口响应不是合法 JSON。\n"
                f"{_response_detail(res)}"
            ) from exc

    with allure.step("断言响应结构"):
        assert isinstance(body, dict), (
            "新币列表接口响应主体类型错误，期望 dict。\n"
            f"{_response_detail(res)}"
        )
        assert "code" in body, (
            "新币列表接口响应缺少 code 字段。\n"
            f"响应字段: {list(body.keys())}\n"
            f"{_response_detail(res)}"
        )
        assert "data" in body, (
            "新币列表接口响应缺少 data 字段。\n"
            f"响应字段: {list(body.keys())}\n"
            f"{_response_detail(res)}"
        )
        assert body["code"] == 200, (
            "新币列表接口业务 code 异常，期望 200。\n"
            f"实际 code: {body.get('code')}\n"
            f"{_response_detail(res)}"
        )

        data = body["data"]
        assert isinstance(data, dict), (
            "新币列表接口 data 类型错误，期望 dict。\n"
            f"实际类型: {type(data).__name__}\n"
            f"{_response_detail(res)}"
        )
        assert "total" in data, (
            "新币列表接口 data 缺少 total 字段。\n"
            f"data字段: {list(data.keys())}\n"
            f"{_response_detail(res)}"
        )
        assert "rows" in data, (
            "新币列表接口 data 缺少 rows 字段。\n"
            f"data字段: {list(data.keys())}\n"
            f"{_response_detail(res)}"
        )

        total = data["total"]
        rows = data["rows"]
        assert isinstance(total, int), (
            "新币列表接口 data.total 类型错误，期望 int。\n"
            f"实际类型: {type(data['total']).__name__}\n"
            f"{_response_detail(res)}"
        )
        assert isinstance(rows, list), (
            "新币列表接口 data.rows 类型错误，期望 list。\n"
            f"实际类型: {type(rows).__name__}\n"
            f"{_response_detail(res)}"
        )
