import requests


def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]
        return {
            "name": data["name"]["common"],
            "capital": data.get("capital", ["N/A"])[0],
            "population": data["population"],
            "area": data.get("area", "N/A"),
            "currencies": ", ".join(data.get("currencies", {}).keys()),
            "languages": ", ".join(data.get("languages", {}).values()),
        }
    elif response.status_code == 404:
        return None
    else:
        raise Exception(f"API request failed with status code {response.status_code}")


def display_country_info(country_info):
    print(f"\nCountry Information for {country_info['name']}:")
    print(f"Capital: {country_info['capital']}")
    print(f"Population: {country_info['population']:,}")
    print(f"Area: {country_info['area']:,} sq km")
    print(f"Currencies: {country_info['currencies']}")
    print(f"Languages: {country_info['languages']}")


def main():
    while True:
        country_name = input("Enter the name of a country (or 'quit' to exit): ")
        if country_name.lower() == "quit":
            break

        try:
            country_info = fetch_country_data(country_name)
            if country_info:
                display_country_info(country_info)
            else:
                print(f"Country '{country_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
