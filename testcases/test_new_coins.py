from public.request import ApiClient


def test_new_coins(base_url, headers):
    client = ApiClient(base_url, headers)
    res = client.get(
        "/xh-gather-app/app/market/currency/v1/open/page/newCoins",
        params={"pageNum": 1, "pageSize": 10},
    )

    assert res.status_code == 200
    assert res.json()["code"] == 200
