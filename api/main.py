import requests
import json
    
def main():

    URL = "https://openlibrary.org"

    SEARCH_ENDPOINT = "/search.json?q=test"
    ENDPOINT = "/subjects/Fantasy.json"

    headers = {
        "User-Agent": "open-library-api-data-pipeline (jakobgrob9@gmail.com)"
    }

    params = {
        "language": "en",
        "limit": 10
    }

    response = requests.get(
        URL + ENDPOINT,
        params=params, 
        headers=headers)

    data = response.json()

    with open('fantasyData.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Hello from financial-api-data-pipeline!")


if __name__ == "__main__":
    main()
