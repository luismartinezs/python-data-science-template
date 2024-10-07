import requests

url = "https://jsonplaceholder.typicode.com/posts"


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


# print(request_with_error_handling(url))

# print(request_with_error_handling("https://api.nonexistent.com/data")["success"])

response = request_with_error_handling(
    url, method="POST", data={"title": "New Post", "body": "This is a new post"}
)

if response["success"]:
    print(response["data"])
else:
    print(response["error"])

