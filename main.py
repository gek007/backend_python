import requests

url = "https://api.hh.ru/vacancies"


def fetch_hh_vacancies(url: str):

    query_param = {
        "text": "diango OR fastapi OR aiohttp OR litestar OR flask",
        "per_page":100,
        "page":0,
    }

    requests.get(url=url, params=query_param)



