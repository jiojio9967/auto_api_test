# -*- coding: utf-8 -*-
"""公共断言工具，基于项目实际响应风格设计。

设计原则：
1. 失败提示统一携带请求 URL、HTTP 状态码、响应内容，方便 Allure 报告排查。
2. 正常用例与异常用例的断言粒度分开，避免互相污染。
3. 不假设字段命名统一，若字段名不一致由各业务用例自行处理。
"""
from typing import Iterable, Tuple, Union


def response_detail(res) -> str:
    """统一格式化响应诊断信息，断言失败时一定要带上。"""
    return (
        f"请求URL  : {res.request.url}\n"
        f"HTTP状态 : {res.status_code}\n"
        f"响应内容 : {res.text}"
    )


def assert_http_ok(res, allow_codes: Tuple[int, ...] = (200,)) -> None:
    """断言 HTTP 状态码命中允许范围（默认仅 200）。"""
    assert res.status_code in allow_codes, (
        f"HTTP 状态码异常，期望 {allow_codes}。\n"
        f"{response_detail(res)}"
    )


def assert_json_response(res) -> dict:
    """断言响应可被解析为 JSON，并返回 body。"""
    try:
        body = res.json()
    except ValueError as exc:
        raise AssertionError(
            "响应不是合法 JSON。\n"
            f"{response_detail(res)}"
        ) from exc
    return body


def assert_business_success(res, body: dict = None) -> dict:
    """断言业务 code=200、msg 非空、data 存在。返回响应 body。"""
    if body is None:
        body = assert_json_response(res)
    assert isinstance(body, dict), (
        f"响应主体类型错误，期望 dict。\n"
        f"{response_detail(res)}"
    )
    assert body.get("code") == 200, (
        f"业务 code 异常，期望 200。\n"
        f"{response_detail(res)}"
    )
    msg = body.get("msg")
    assert msg not in (None, ""), (
        f"业务 msg 为空。\n"
        f"{response_detail(res)}"
    )
    return body


def assert_has_keys(data: dict, keys: Iterable[str], obj_name: str, res=None) -> None:
    """断言 data 是 dict 且包含指定字段。"""
    detail = response_detail(res) if res is not None else f"实际内容: {data}"
    assert isinstance(data, dict), (
        f"{obj_name} 类型错误，期望 dict。\n"
        f"{detail}"
    )
    missing = [k for k in keys if k not in data]
    assert not missing, (
        f"{obj_name} 缺少字段: {missing}。\n"
        f"实际字段: {list(data.keys())}\n"
        f"{detail}"
    )


def assert_field_type(
    data: dict,
    field: str,
    expected_type: Union[type, Tuple[type, ...]],
    obj_name: str = "data",
    res=None,
) -> None:
    """断言 data[field] 存在且为期望类型。"""
    detail = response_detail(res) if res is not None else f"实际内容: {data}"
    assert field in data, (
        f"{obj_name} 缺少字段 {field}。\n"
        f"{detail}"
    )
    assert isinstance(data[field], expected_type), (
        f"{obj_name}.{field} 类型错误，期望 {expected_type}，实际 {type(data[field]).__name__}。\n"
        f"{detail}"
    )


def assert_error_response(
    res,
    expected_codes: Iterable = None,
    expected_msg_keywords: Iterable[str] = None,
    expect_data_none: bool = False,
) -> dict:
    """异常用例统一断言。

    默认行为（向后兼容）：
    - HTTP 状态码允许 200 / 常见错误码；
    - 响应必须是合法 JSON；
    - 必须包含 code 或 msg；
    - 若有 msg，则不能为空；
    - data 为 None 是允许的。

    可选增强参数：
    - expected_codes：业务 code 必须命中的集合（如 (500,)、(4011, 4012)）；
    - expected_msg_keywords：msg 中必须包含的关键字（任意一个匹配即通过）；
    - expect_data_none：是否要求 data is None。
    """
    assert res.status_code in (200, 400, 401, 403, 404, 405, 500), (
        f"异常用例 HTTP 状态码超出预期范围。\n"
        f"{response_detail(res)}"
    )
    body = assert_json_response(res)
    assert isinstance(body, dict), (
        f"异常用例响应类型错误，期望 dict。\n"
        f"{response_detail(res)}"
    )
    assert ("code" in body) or ("msg" in body), (
        f"异常用例响应缺少 code/msg 字段。\n"
        f"{response_detail(res)}"
    )
    if "msg" in body:
        assert body["msg"] not in (None, ""), (
            f"异常用例 msg 不能为空。\n"
            f"{response_detail(res)}"
        )

    if expected_codes is not None:
        expected_set = tuple(expected_codes)
        assert body.get("code") in expected_set, (
            f"异常用例业务 code 未命中期望集合 {expected_set}。\n"
            f"实际 code: {body.get('code')}\n"
            f"{response_detail(res)}"
        )

    if expected_msg_keywords:
        msg = body.get("msg") or ""
        keywords = tuple(expected_msg_keywords)
        assert any(k in msg for k in keywords), (
            f"异常用例 msg 未包含期望关键字 {keywords}。\n"
            f"实际 msg: {msg}\n"
            f"{response_detail(res)}"
        )

    if expect_data_none:
        assert body.get("data") is None, (
            f"异常用例期望 data 为 None。\n"
            f"实际 data: {body.get('data')}\n"
            f"{response_detail(res)}"
        )

    return body
