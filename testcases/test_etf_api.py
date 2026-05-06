import allure

from public.request import ApiClient


ETF_PAGE_PATH = "/xhj-gather-app/open/etf/page"
ETF_STATISTICS_PATH = "/xhj-gather-app/open/etf/statistics"
ETF_SEARCH_RELATED_PATH = "/xhj-gather-app/open/etf/searchRelated"


def _response_detail(res):
    return (
        f"请求URL  : {res.request.url}\n"
        f"HTTP状态 : {res.status_code}\n"
        f"响应内容 : {res.text}"
    )


def _assert_status_code(res):
    assert res.status_code == 200, (
        "ETF接口 HTTP 状态码异常。\n"
        f"{_response_detail(res)}"
    )


def _assert_json_response(res):
    try:
        body = res.json()
    except ValueError as exc:
        raise AssertionError(
            "ETF接口响应不是合法 JSON。\n"
            f"{_response_detail(res)}"
        ) from exc

    assert isinstance(body, dict), (
        "ETF接口响应主体类型错误，期望 dict。\n"
        f"{_response_detail(res)}"
    )
    assert "data" in body, (
        "ETF接口响应缺少 data 字段。\n"
        f"响应字段: {list(body.keys())}\n"
        f"{_response_detail(res)}"
    )

    data = body["data"]
    if isinstance(data, list):
        assert isinstance(data, list), (
            "ETF接口 data 字段类型错误，期望 list。\n"
            f"{_response_detail(res)}"
        )

    return body


@allure.title("ETF分页列表接口")
@allure.description("请求 App 实际使用的 ETF 分页列表接口，校验 HTTP 状态码、JSON 解析和基础响应结构。")
def test_etf_page(base_url, headers):
    with allure.step("创建客户端"):
        client = ApiClient(base_url, headers)

    with allure.step("发送请求"):
        res = client.get(
            ETF_PAGE_PATH,
            params={"asc": 0, "limit": 20, "locale": "us", "page": 1},
        )

    with allure.step("断言状态码"):
        _assert_status_code(res)

    with allure.step("断言响应结构"):
        _assert_json_response(res)


@allure.title("ETF统计接口-type=1")
@allure.description("请求 App 实际使用的 ETF 统计接口 type=1，校验 HTTP 状态码、JSON 解析和基础响应结构。")
def test_etf_statistics_type_1(base_url, headers):
    with allure.step("创建客户端"):
        client = ApiClient(base_url, headers)

    with allure.step("发送请求"):
        res = client.get(ETF_STATISTICS_PATH, params={"locale": "us", "type": 1})

    with allure.step("断言状态码"):
        _assert_status_code(res)

    with allure.step("断言响应结构"):
        _assert_json_response(res)


@allure.title("ETF统计接口-type=2")
@allure.description("请求 App 实际使用的 ETF 统计接口 type=2，校验 HTTP 状态码、JSON 解析和基础响应结构。")
def test_etf_statistics_type_2(base_url, headers):
    with allure.step("创建客户端"):
        client = ApiClient(base_url, headers)

    with allure.step("发送请求"):
        res = client.get(ETF_STATISTICS_PATH, params={"locale": "us", "type": 2})

    with allure.step("断言状态码"):
        _assert_status_code(res)

    with allure.step("断言响应结构"):
        _assert_json_response(res)


@allure.title("ETF相关推荐接口-type=1")
@allure.description("请求 App 实际使用的 ETF 相关推荐接口 type=1，校验 HTTP 状态码、JSON 解析和基础响应结构。")
def test_etf_search_related_type_1(base_url, headers):
    with allure.step("创建客户端"):
        client = ApiClient(base_url, headers)

    with allure.step("发送请求"):
        res = client.get(ETF_SEARCH_RELATED_PATH, params={"type": 1})

    with allure.step("断言状态码"):
        _assert_status_code(res)

    with allure.step("断言响应结构"):
        _assert_json_response(res)


@allure.title("ETF相关推荐接口-type=2")
@allure.description("请求 App 实际使用的 ETF 相关推荐接口 type=2，校验 HTTP 状态码、JSON 解析和基础响应结构。")
def test_etf_search_related_type_2(base_url, headers):
    with allure.step("创建客户端"):
        client = ApiClient(base_url, headers)

    with allure.step("发送请求"):
        res = client.get(ETF_SEARCH_RELATED_PATH, params={"type": 2})

    with allure.step("断言状态码"):
        _assert_status_code(res)

    with allure.step("断言响应结构"):
        _assert_json_response(res)
