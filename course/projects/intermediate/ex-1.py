import requests

base_url = "https://jsonplaceholder.typicode.com/"
resources = {
    "posts": "posts",
    "users": "users",
}


def request_with_error_handling(url, method="GET", data=None):
    try:
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json=data)
        else:
            return {"success": False, "error": "Unsupported HTTP method"}

        response.raise_for_status()  # Will raise an HTTPError for bad responses
        return {"success": True, "data": response.json()}
    except requests.exceptions.HTTPError as err:
        return {"success": False, "error": f"HTTP error occurred: {err}"}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "Error connecting to the server"}
    except Exception as e:
        return {"success": False, "error": f"An error occurred: {e}"}


def fetch_data(url: str) -> dict:
    response = request_with_error_handling(url)
    if response["success"]:
        return response["data"]
    else:
        print(response["error"])
        return None


def get_posts():
    url = base_url + resources["posts"]
    return fetch_data(url)


def get_users():
    url = base_url + resources["users"]
    return fetch_data(url)


def display_posts(posts: list[dict]):
    for post in posts:
        print(post)


def display_users(users: list[dict]):
    for user in users:
        print(user)


post_titles = [post["title"] for post in get_posts()]
display_posts(post_titles)
