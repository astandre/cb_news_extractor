import requests
import os

TOKEN = os.environ.get("FB_TOKEN")


BASE_URL = f"https://graph.facebook.com/"


def get_posts():
    url = f"{BASE_URL}/me/feed?access_token={TOKEN}"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            response = r.json()
            return response["data"]
    except requests.exceptions.RequestException as e:
        print(e)


def get_post(post_id):
    url = f"{BASE_URL}/{post_id}?fields=full_picture,is_published,message,shares,permalink_url.limit(1)&access_token={TOKEN}"
    try:
        r = requests.get(url)
        # print(r)
        response = r.json()
        # print(response)
        if r.status_code == 200:
            response = r.json()
            return response

    except requests.exceptions.RequestException as e:
        print(e)
