# -*- coding: utf-8 -*-
import allure

from public.request import ApiClient


NEW_COINS_PATH = "/xh-gather-app/app/market/currency/v1/open/page/newCoins"
NEW_COINS_PARAMS = {"pageNum": 1, "pageSize": 10}
REQUIRED_RESPONSE_KEYS = ("code", "data")
REQUIRED_PAGE_KEYS = ("list", "total", "pageNum", "pageSize")


def _response_detail(res):
    return (
        f"请求URL  : {res.request.url}\n"
        f"HTTP状态 : {res.status_code}\n"
        f"响应内容 : {res.text}"
    )


def _assert_has_keys(data, keys, obj_name):
    assert isinstance(data, dict), (
        f"{obj_name} 类型错误，期望 dict，实际为 {type(data).__name__}。\n"
        f"实际内容: {data}"
    )

    missing_keys = [key for key in keys if key not in data]
    assert not missing_keys, (
        f"{obj_name} 缺少必要字段: {missing_keys}。\n"
        f"实际字段: {list(data.keys())}\n"
        f"实际内容: {data}"
    )


def _assert_not_empty(value, field_name, source):
    assert value not in (None, "", [], {}), (
        f"{field_name} 不能为空。\n"
        f"字段值: {value}\n"
        f"来源数据: {source}"
    )


def _assert_any_not_empty(data, field_names, field_desc):
    exists_fields = [field for field in field_names if field in data]
    assert exists_fields, (
        f"币种数据缺少{field_desc}字段，候选字段: {field_names}。\n"
        f"实际字段: {list(data.keys())}\n"
        f"实际内容: {data}"
    )

    not_empty_fields = [field for field in exists_fields if data.get(field) not in (None, "", [], {})]
    assert not_empty_fields, (
        f"币种数据{field_desc}字段存在但均为空，候选字段: {field_names}。\n"
        f"实际内容: {data}"
    )


@allure.title("新币列表接口")
@allure.description(
    "请求新币分页列表接口，校验 HTTP 状态码、JSON 解析、响应主结构、data/list/分页字段以及币种核心字段。"
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
            "新币列表接口 HTTP 状态码异常，当前接口真实返回非 200，未继续执行 JSON/结构断言。\n"
            "如果这里返回 404，请优先确认接口路径、网关前缀或服务路由是否正确。\n"
            f"{_response_detail(res)}"
        )

    with allure.step("断言响应可以解析为 JSON"):
        try:
            body = res.json()
        except ValueError as exc:
            raise AssertionError(
                "新币列表接口响应不是合法 JSON。\n"
                f"{_response_detail(res)}"
            ) from exc

    with allure.step("断言响应主结构包含 code 和 data"):
        _assert_has_keys(body, REQUIRED_RESPONSE_KEYS, "响应主体")
        assert body["code"] == 200, (
            "新币列表接口业务 code 异常，期望 200。\n"
            f"实际 code: {body.get('code')}\n"
            f"完整响应: {body}"
        )

    with allure.step("断言 data 为分页对象且包含 list/分页字段"):
        data = body["data"]
        _assert_has_keys(data, REQUIRED_PAGE_KEYS, "data")

        coin_list = data["list"]
        assert isinstance(coin_list, list), (
            "data.list 类型错误，期望 list。\n"
            f"实际类型: {type(coin_list).__name__}\n"
            f"data 内容: {data}"
        )
        _assert_not_empty(coin_list, "data.list", data)

        assert isinstance(data["total"], int), (
            "data.total 类型错误，期望 int。\n"
            f"实际类型: {type(data['total']).__name__}\n"
            f"data 内容: {data}"
        )
        assert data["total"] >= len(coin_list), (
            "data.total 不能小于当前 list 长度。\n"
            f"total: {data['total']}, list长度: {len(coin_list)}\n"
            f"data 内容: {data}"
        )
        assert data["pageNum"] == NEW_COINS_PARAMS["pageNum"], (
            "data.pageNum 与请求参数不一致。\n"
            f"请求 pageNum: {NEW_COINS_PARAMS['pageNum']}, 响应 pageNum: {data['pageNum']}\n"
            f"data 内容: {data}"
        )
        assert data["pageSize"] == NEW_COINS_PARAMS["pageSize"], (
            "data.pageSize 与请求参数不一致。\n"
            f"请求 pageSize: {NEW_COINS_PARAMS['pageSize']}, 响应 pageSize: {data['pageSize']}\n"
            f"data 内容: {data}"
        )

    with allure.step("断言币种核心字段存在且非空"):
        first_coin = coin_list[0]
        assert isinstance(first_coin, dict), (
            "data.list 第一条数据类型错误，期望 dict。\n"
            f"实际类型: {type(first_coin).__name__}\n"
            f"第一条数据: {first_coin}"
        )
        _assert_any_not_empty(first_coin, ("id", "currencyId", "coinId"), "ID")
        _assert_any_not_empty(first_coin, ("symbol", "coinSymbol", "currencySymbol"), "币种简称")
        _assert_any_not_empty(first_coin, ("name", "coinName", "currencyName"), "币种名称")
