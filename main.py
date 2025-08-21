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

def main():
    res = fetch_hh_vacancies(url=url)
    print(res)

if __name__ == "__main__":
      main()




