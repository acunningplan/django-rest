import requests

headers = {}
headers["Authentication"] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYyMzMyNzIxLCJqdGkiOiJiZDU0OTJjMjM0Njg0NTM2YjBmYzE5NWNlZDFlN2FlNiIsInVzZXJfaWQiOjF9.v4lXUIuWHbZceTXrI7XP1HxS9poyEZ6kNoZoRPdd76I'

r = requests.get("http://127.0.0.1:8000/paradigm", headers=headers)

print(r.text)
