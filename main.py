import json
import time

import requests

url = "https://api.hh.ru/vacancies"


def fetch_hh_vacancies(url: str, page: int = 0):

    query_param = {
        "text": "diango OR fastapi OR aiohttp OR litestar OR flask",
        "per_page":100,
        "page":page,
    }

    resp = requests.get(url=url, params=query_param)
    if resp.status_code != 200:
        print(f"Error reply { resp.status_code= }")
    json_data = resp.json()
    return json_data

def fetch_all_hh_vacancies(url: str):
    page = 0
    result = []
    while True:
        print(f"Fetching page { page }")
        res = fetch_hh_vacancies(url=url, page=page)
        result.extend(res)
        if page == 5:
            break
        page += 1
        time.sleep(0.5)

    with open("hh_vacancies.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)


def main():
    res = fetch_all_hh_vacancies(url=url)
    print(res)


if __name__ == "__main__":
      main()




