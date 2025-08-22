import json
import time
import functools
import requests
from dataclasses import dataclass
from typing import Optional

url = "https://api.hh.ru/vacancies"



@dataclass
class VacancyData:
    title: str
    salary: Optional[str]
    url: str

#this example

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry decorator.

    :param max_attempts: number of attempts before giving up
    :param delay: seconds to wait between attempts
    :param exceptions: tuple of exceptions to catch and retry on
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < max_attempts:
                        time.sleep(delay)
                    else:
                        raise  # re-raise last exception

        return wrapper

    return decorator

@retry(max_attempts=5, delay=2, exceptions=(ValueError,))
def fetch_hh_vacancies(url: str, page: int = 0):

    query_param = {
        "text": "diango OR fastapi OR aiohttp OR litestar OR flask",
        "per_page":100,
        "page":page,
    }

    resp = requests.get(url=url, params=query_param)
    if resp.status_code != 200:
        print(f"Error reply { resp.status_code= }")
        raise ValueError(f"Error reply { resp.status_code= }")
    json_data = resp.json()
    items = json_data["items"]

    for item in items:

        _salary = None
        if item.get("salary"):
            salary = f"{item['salary'].get('from')} - {item['salary'].get('to')} {item['salary'].get('currency')}"

        vacancy = VacancyData(
            title =item["name"],
            salary = _salary,
            url = item["alternate_url"],
        )

        print(vacancy)


    return json_data

def fetch_all_hh_vacancies(url: str):
    page = 0
    result = []
    while True:
        print(f"Fetching page { page= }")
        res = fetch_hh_vacancies(url=url, page=page)

        if (page == 5) or len(res) == 0:
            break

        result.extend(res)
        page += 1
        time.sleep(0.5)

    with open("hh_vacancies.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False))


def main():
    res = fetch_all_hh_vacancies(url=url)
    print(f"result {res=}")
    print(f"finish")

if __name__ == "__main__":
      main()




