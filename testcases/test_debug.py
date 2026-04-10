def test_debug_notice(client):
    res = client.post("/xhj-gather-app/notice/count")

    print("\n返回内容：", res.text)

    assert res.status_code == 200