import requests


print("Input the URL:")
url = input()
try:
    result = requests.get(url)
    print(result.json()['content'])
except KeyError as e:
    print("Invalid quote resource!")

