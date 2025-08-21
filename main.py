import requests

url = "https://api.hh.ru/vacancies"


def fetch_hh_vacancies(url: str, page: int = 0):

    query_param = {
        "text": "diango OR fastapi OR aiohttp OR litestar OR flask",
        "per_page":100,
        "page":page,
    }

    resp = requests.get(url=url, params=query_param)
    json_data = resp.json()



