# -*- coding: utf-8 -*-
"""用户/会员模块接口用例。

包含：通知、会员资料、会员关注/邀请/拉黑、社区互动、收藏、活动奖励、创作者等。
原 test_auto_api.py 中相关用例搬运至此，已通过的断言保持不变。
"""
import allure
import pytest
import requests

from public.assertions import (
    assert_business_success,
    assert_error_response,
    assert_field_type,
    assert_http_ok,
    response_detail,
)
from public.headers import get_headers


pytestmark = [allure.epic("用户会员模块")]


MEMBER_FOLLOW_PATH = "/xhj-gather-app/memberFollow/page"


# ────────────────────────── 通知 ──────────────────────────


@allure.feature("消息通知")
@allure.story("正常查询")
@allure.title("通知未读数接口")
def test_notice_count(client):
    res = client.get("/xhj-gather-app/notice/count")
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("消息通知")
@allure.story("正常查询")
@allure.title("评论通知分页接口")
def test_notice_comment_page(client):
    res = client.get("/xhj-gather-app/notice/commentPage", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("消息通知")
@allure.story("正常查询")
@allure.title("点赞通知分页接口")
def test_notice_like_page(client):
    res = client.get("/xhj-gather-app/notice/likePage", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 会员资料 ──────────────────────────


@allure.feature("会员资料")
@allure.story("正常查询")
@allure.title("获取会员基础信息")
def test_member_info(client):
    res = client.get("/xhj-gather-app/member/info")
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("会员账户")
@allure.story("正常查询")
@allure.title("查询会员积分余额")
def test_member_account_point(client):
    res = client.get("/xhj-gather-app/memberAccount/getPoint")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 会员关注 ──────────────────────────


@allure.feature("关注列表")
@allure.story("正常查询")
@allure.title("会员关注列表分页接口")
@allure.description("会员关注列表分页接口使用 POST 请求，分页参数放在 JSON Body 中。")
def test_member_follow_page(client):
    body = {
        "page": 1,
        "orderType": 1,
        "createBy": 120554,
        "limit": 20,
        "selType": 1,
    }

    with allure.step("发送会员关注列表分页请求"):
        res = client.post(MEMBER_FOLLOW_PATH, json=body)

    with allure.step("断言 HTTP 状态码"):
        assert_http_ok(res)

    with allure.step("解析并断言响应主结构"):
        res_body = assert_business_success(res)
        assert isinstance(res_body.get("data"), dict), (
            "会员关注列表分页接口 data 类型错误，期望 dict。\n"
            f"{response_detail(res)}"
        )

    with allure.step("断言分页字段"):
        data = res_body["data"]
        assert_field_type(data, "totalCount", int, "data", res)
        assert_field_type(data, "pageSize", int, "data", res)
        assert_field_type(data, "totalPage", int, "data", res)
        assert data.get("currPage") == body["page"], (
            "会员关注列表分页接口 data.currPage 缺失或与请求 page 不一致。\n"
            f"{response_detail(res)}"
        )
        assert_field_type(data, "list", list, "data", res)

    with allure.step("如果列表不为空，断言第一条关注数据字段"):
        if data["list"]:
            first_item = data["list"][0]
            assert isinstance(first_item, dict), (
                "会员关注列表分页接口 data.list 第一条数据类型错误，期望 dict。\n"
                f"{response_detail(res)}"
            )
            for field in ("id", "memberId", "status", "nickname", "memberType", "createTime"):
                assert field in first_item, (
                    f"会员关注列表分页接口第一条数据缺少字段: {field}。\n"
                    f"{response_detail(res)}"
                )


@allure.feature("关注列表")
@allure.story("参数异常")
@pytest.mark.parametrize(
    "json_body, case_name",
    [
        ({}, "请求体为空"),
        (
            {"page": "abc", "limit": 10, "orderType": 1, "createBy": 120554, "selType": 1},
            "page类型错误",
        ),
        (
            {"page": 1, "limit": "abc", "orderType": 1, "createBy": 120554, "selType": 1},
            "limit类型错误",
        ),
    ],
    ids=["请求体为空", "page类型错误", "limit类型错误"],
)
def test_member_follow_page_invalid_body(client, json_body, case_name):
    """实测：上述异常 body 接口返回 code=500, msg=服务繁忙，请稍后再试，data is None。"""
    allure.dynamic.title(f"会员关注列表 - 参数异常 - {case_name}")

    with allure.step(f"发送异常请求：{case_name}"):
        res = client.post(MEMBER_FOLLOW_PATH, json=json_body)

    with allure.step("断言已知服务端500场景：code=500 + msg含'服务繁忙' + data is None"):
        assert_error_response(
            res,
            expected_codes=(500,),
            expected_msg_keywords=("服务繁忙",),
            expect_data_none=True,
        )


@allure.feature("关注列表")
@allure.story("边界值")
@pytest.mark.parametrize(
    "json_body, case_name",
    [
        (
            {"page": -1, "limit": 10, "orderType": 1, "createBy": 120554, "selType": 1},
            "page为负数",
        ),
        (
            {"page": 1, "limit": 0, "orderType": 1, "createBy": 120554, "selType": 1},
            "limit为0",
        ),
        (
            {"page": 1, "limit": 100, "orderType": 1, "createBy": 120554, "selType": 1},
            "limit为100",
        ),
    ],
    ids=["page为负数", "limit为0", "limit为100"],
)
def test_member_follow_page_boundary(client, json_body, case_name):
    """实测：服务端对 page<=0/limit=0 等边界值兼容处理，仍返回 code=200。"""
    allure.dynamic.title(f"会员关注列表 - 边界值 - {case_name}")

    with allure.step(f"发送边界值请求：{case_name}"):
        res = client.post(MEMBER_FOLLOW_PATH, json=json_body)

    with allure.step("断言响应基础结构"):
        assert_http_ok(res)
        body = assert_business_success(res)
        assert isinstance(body.get("data"), dict), (
            f"边界值 {case_name} 下 data 期望 dict。\n"
            f"{response_detail(res)}"
        )


@allure.feature("关注列表")
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
def test_member_follow_page_unauthorized(base_url, auth_value, case_name, expected_codes):
    allure.dynamic.title(f"会员关注列表 - 未登录 - {case_name}")
    headers = dict(get_headers())
    if auth_value is None:
        headers.pop("authorization", None)
    else:
        headers["authorization"] = auth_value

    body = {
        "page": 1,
        "orderType": 1,
        "createBy": 120554,
        "limit": 20,
        "selType": 1,
    }

    with allure.step(f"使用 {case_name} 直接请求接口"):
        res = requests.post(
            f"{base_url}{MEMBER_FOLLOW_PATH}",
            json=body,
            headers=headers,
            timeout=15,
        )

    with allure.step(f"断言未登录场景：code 命中 {expected_codes} + data is None"):
        assert_error_response(
            res,
            expected_codes=expected_codes,
            expect_data_none=True,
        )


# ────────────────────────── 邀请 / 拉黑 ──────────────────────────


@allure.feature("邀请")
@allure.story("正常查询")
@allure.title("我的邀请分页接口")
def test_member_invited_page(client):
    res = client.get("/xhj-gather-app/memberInvited/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("邀请")
@allure.story("正常查询")
@allure.title("邀请统计接口")
def test_member_invited_statistics(client):
    res = client.get("/xhj-gather-app/memberInvited/statistics")
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("拉黑")
@allure.story("正常查询")
@allure.title("黑名单分页接口")
def test_member_black_page(client):
    res = client.get("/xhj-gather-app/memberBlack/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 社区内容 ──────────────────────────


@allure.feature("社区动态")
@allure.story("正常查询")
@allure.title("我评论的动态分页接口")
def test_community_content_comment_page(client):
    res = client.get(
        "/xhj-gather-app/community/content/commentPage",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("社区动态")
@allure.story("正常查询")
@allure.title("我点赞的动态分页接口")
def test_community_content_like_page(client):
    res = client.get(
        "/xhj-gather-app/community/content/likePage",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("社区动态")
@allure.story("正常查询")
@allure.title("我收藏的动态分页接口")
def test_community_content_collect_page(client):
    res = client.get(
        "/xhj-gather-app/community/contentCollect/page",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("话题关注")
@allure.story("正常查询")
@allure.title("话题关注分页接口")
def test_community_topic_follow_page(client):
    res = client.get(
        "/xhj-gather-app/community/topicFollow/page",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 文章/快讯收藏 ──────────────────────────


@allure.feature("文章收藏")
@allure.story("正常查询")
@allure.title("文章收藏分页接口")
def test_article_collect_page(client):
    res = client.get(
        "/xhj-gather-app/articleCollect/page",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("快讯收藏")
@allure.story("正常查询")
@allure.title("快讯收藏分页接口")
def test_cms_newsflash_collect_page(client):
    res = client.get(
        "/xhj-gather-app/cmsNewsFlashCollect/collectPage",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 活动奖励 ──────────────────────────


@allure.feature("活动奖励")
@allure.story("已知服务端500")
@allure.title("中奖列表分页接口")
@pytest.mark.xfail(
    reason="服务端真实返回 code=500，待确认真实 App 请求方式或接口状态。",
    strict=False,
)
def test_member_activity_reward_page(client):
    res = client.get(
        "/xhj-gather-app/memberActivityReward/page",
        params={"page": 1, "limit": 10},
    )
    assert_business_success(res)


@allure.feature("活动奖励")
@allure.story("正常查询")
@allure.title("免费抽奖未读通知接口")
def test_member_activity_reward_free_draw_unread(client):
    res = client.get("/xhj-gather-app/memberActivityReward/queryFreeDrawNoticeUnread")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 创作者 ──────────────────────────


@allure.feature("创作者")
@allure.story("正常查询")
@allure.title("创作者内容分页接口")
def test_creator_content_page(client):
    res = client.get(
        "/xhj-gather-app/creatorContent/page",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("创作者")
@allure.story("正常查询")
@allure.title("创作者详情接口")
def test_member_creator_detail(client):
    res = client.get("/xhj-gather-app/memberCreator/detail")
    assert res.status_code == 200
    assert res.json()["code"] == 200
