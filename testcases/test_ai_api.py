# -*- coding: utf-8 -*-
"""AI 模块接口用例。

包含 AI 聊天记录、AI 提示词、AI 默认提问语等接口。
正常用例搬运自原 test_auto_api.py 的相关分组。
"""
import allure


pytestmark = [allure.epic("AI模块")]


# ────────────────────────── 聊天记录 ──────────────────────────


@allure.feature("聊天记录")
@allure.story("正常查询")
@allure.title("AI 问答未读数接口")
def test_chat_unread_num(client):
    res = client.get("/xhj-gather-app/chatRecord/getUnreadNum")
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("聊天记录")
@allure.story("正常查询")
@allure.title("AI 问答记录分页接口")
def test_chat_member_record_page(client):
    res = client.get(
        "/xhj-gather-app/chatRecord/getChatMemberRecordPage",
        params={"page": 1, "limit": 10},
    )
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("聊天记录")
@allure.story("正常更新")
@allure.title("AI 问答全部已读接口")
def test_chat_put_all_read(client):
    res = client.post("/xhj-gather-app/chatRecord/putAllRead")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── AI 提示词 ──────────────────────────


@allure.feature("AI提示词")
@allure.story("正常查询")
@allure.title("AI 提示词列表接口")
def test_cue_word_query_list(client):
    res = client.get("/xhj-gather-app/cueWord/getQueryList")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── AI 默认提问 ──────────────────────────


@allure.feature("默认消息")
@allure.story("正常查询")
@allure.title("默认提问语列表接口")
def test_default_message_list(client):
    res = client.get("/xhj-gather-app/defaultMessage/list")
    assert res.status_code == 200
    assert res.json()["code"] == 200
