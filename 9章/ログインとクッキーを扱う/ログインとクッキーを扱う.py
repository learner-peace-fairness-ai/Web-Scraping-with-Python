import requests

WELCOME_PAGE_URL = "https://pythonscraping.com/pages/cookies/welcome.php"
PROFILE_PAGE_URL = "https://pythonscraping.com/pages/cookies/profile.php"
PARAMS = {"username": "Ryan", "password": "password"}

res = requests.post(WELCOME_PAGE_URL, data=PARAMS)
print("Cookie is set to:")
print(res.cookies.get_dict())
print("----------")
print("Going to profile page...")

res = requests.get(PROFILE_PAGE_URL, cookies=res.cookies)
print(res.text)
