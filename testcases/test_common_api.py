# -*- coding: utf-8 -*-
"""通用模块接口用例。

包含暂时无法明确归类的接口：CMS 标签、标签分页、任务中心、举报字典等。
正常用例搬运自原 test_auto_api.py。
"""
import allure
import pytest

from public.assertions import assert_business_success


pytestmark = [allure.epic("通用模块")]


# ────────────────────────── 标签 ──────────────────────────


@allure.feature("CMS标签")
@allure.story("正常查询")
@allure.title("获取 CMS 标签列表")
def test_cms_tag_list(client):
    res = client.get("/xhj-gather-app/cms/tag/stateless/getTagList")
    assert res.status_code == 200
    assert res.json()["code"] == 200


@allure.feature("标签分页")
@allure.story("已知服务端500")
@allure.title("标签分页列表接口")
@pytest.mark.xfail(
    reason="服务端真实返回 code=500，待业务确认。",
    strict=False,
)
def test_label_page(client):
    res = client.get("/xhj-gather-app/label/page", params={"page": 1, "limit": 10})
    assert_business_success(res)


# ────────────────────────── 任务中心 ──────────────────────────


@allure.feature("任务中心")
@allure.story("正常查询")
@allure.title("任务中心-浏览时长配置")
def test_task_center_browse_sec(client):
    res = client.get("/xhj-gather-app/taskCenter/getBrowseSec")
    assert res.status_code == 200
    assert res.json()["code"] == 200


# ────────────────────────── 举报 ──────────────────────────


@allure.feature("举报")
@allure.story("正常查询")
@allure.title("举报字典列表")
def test_report_list(client):
    res = client.get("/xhj-gather-app/report/list")
    assert res.status_code == 200
    assert res.json()["code"] == 200
