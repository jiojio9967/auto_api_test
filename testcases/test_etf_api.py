from public.request import ApiClient


def test_etf_page_default(base_url, headers):
    client = ApiClient(base_url, headers)
    res = client.get("/xh-gather-app/open/etf/page", params={"page": 1, "limit": 10})

    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_etf_page_btc_type(base_url, headers):
    client = ApiClient(base_url, headers)
    res = client.get("/xh-gather-app/open/etf/page", params={"page": 1, "limit": 5, "type": 1})

    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_etf_inflow_chart(base_url, headers):
    client = ApiClient(base_url, headers)
    res = client.post(
        "/xh-gather-app/open/etf/inFlowUsdChart",
        json={"page": 1, "limit": 10, "type": 1},
    )

    assert res.status_code == 200
    assert res.json()["code"] == 200
