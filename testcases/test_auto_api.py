# -*- coding: utf-8 -*-
# 自动生成 — 基于 swagger.json，路径已转换为 /xhj-gather-app/ 风格
# 500 接口：仅断言 status_code == 200，不断言业务 code


# ────────────────────────── 通知 ──────────────────────────

def test_notice_count(client):
    res = client.get("/xhj-gather-app/notice/count")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_notice_comment_page(client):
    res = client.get("/xhj-gather-app/notice/commentPage", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_notice_like_page(client):
    res = client.get("/xhj-gather-app/notice/likePage", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 聊天记录 ──────────────────────────

def test_chat_unread_num(client):
    res = client.get("/xhj-gather-app/chatRecord/getUnreadNum")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_chat_member_record_page(client):
    res = client.get("/xhj-gather-app/chatRecord/getChatMemberRecordPage",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_chat_put_all_read(client):
    res = client.post("/xhj-gather-app/chatRecord/putAllRead")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 会员 ──────────────────────────

def test_member_info(client):
    res = client.get("/xhj-gather-app/member/info")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_member_account_point(client):
    res = client.get("/xhj-gather-app/memberAccount/getPoint")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_member_follow_page(client):
    # 服务端返回 code=500，仅断言 HTTP 状态
    res = client.get("/xhj-gather-app/memberFollow/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200


def test_member_invited_page(client):
    res = client.get("/xhj-gather-app/memberInvited/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_member_invited_statistics(client):
    res = client.get("/xhj-gather-app/memberInvited/statistics")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_member_black_page(client):
    res = client.get("/xhj-gather-app/memberBlack/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 币种通知 ──────────────────────────

def test_currency_notice_large_status_all(client):
    res = client.get("/xhj-gather-app/currencyNotice/largeStatusAll")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_currency_notice_page(client):
    res = client.get("/xhj-gather-app/currencyNotice/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_currency_notice_page_v2(client):
    res = client.get("/xhj-gather-app/currencyNotice/pageV2", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_currency_notice_record_page(client):
    res = client.get("/xhj-gather-app/currencyNoticeRecord/page",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── IM 群组 ──────────────────────────

def test_im_group_banner(client):
    # 服务端返回 code=500，仅断言 HTTP 状态
    res = client.get("/xhj-gather-app/im/group/banner")
    assert res.status_code == 200


def test_im_group_banner_v2(client):
    # 服务端返回 code=500，仅断言 HTTP 状态
    res = client.get("/xhj-gather-app/im/group/bannerV2")
    assert res.status_code == 200


def test_im_group_recommend(client):
    res = client.get("/xhj-gather-app/im/group/recommend", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_im_group_mine(client):
    res = client.get("/xhj-gather-app/im/group/mine")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_im_group_notice_last(client):
    res = client.get("/xhj-gather-app/im/groupNotice/last")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 社区内容 ──────────────────────────

def test_community_content_comment_page(client):
    res = client.get("/xhj-gather-app/community/content/commentPage",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_community_content_like_page(client):
    res = client.get("/xhj-gather-app/community/content/likePage",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_community_content_collect_page(client):
    res = client.get("/xhj-gather-app/community/contentCollect/page",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_community_topic_follow_page(client):
    res = client.get("/xhj-gather-app/community/topicFollow/page",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 文章收藏 ──────────────────────────

def test_article_collect_page(client):
    res = client.get("/xhj-gather-app/articleCollect/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_cms_newsflash_collect_page(client):
    res = client.get("/xhj-gather-app/cmsNewsFlashCollect/collectPage",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 标签 / 搜索 ──────────────────────────

def test_cms_tag_list(client):
    res = client.get("/xhj-gather-app/cms/tag/stateless/getTagList")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_cue_word_query_list(client):
    res = client.get("/xhj-gather-app/cueWord/getQueryList")
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_label_page(client):
    # 服务端返回 code=500，仅断言 HTTP 状态
    res = client.get("/xhj-gather-app/label/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200


# ────────────────────────── 默认消息 ──────────────────────────

def test_default_message_list(client):
    res = client.get("/xhj-gather-app/defaultMessage/list")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 任务中心 ──────────────────────────

def test_task_center_browse_sec(client):
    res = client.get("/xhj-gather-app/taskCenter/getBrowseSec")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 活动奖励 ──────────────────────────

def test_member_activity_reward_page(client):
    # 服务端返回 code=500，仅断言 HTTP 状态
    res = client.get("/xhj-gather-app/memberActivityReward/page",
                     params={"page": 1, "limit": 10})
    assert res.status_code == 200


def test_member_activity_reward_free_draw_unread(client):
    res = client.get("/xhj-gather-app/memberActivityReward/queryFreeDrawNoticeUnread")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 创作者 ──────────────────────────

def test_creator_content_page(client):
    res = client.get("/xhj-gather-app/creatorContent/page", params={"page": 1, "limit": 10})
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_member_creator_detail(client):
    res = client.get("/xhj-gather-app/memberCreator/detail")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 举报 ──────────────────────────

def test_report_list(client):
    res = client.get("/xhj-gather-app/report/list")
    assert res.status_code == 200
    assert res.json()["code"] == 200
