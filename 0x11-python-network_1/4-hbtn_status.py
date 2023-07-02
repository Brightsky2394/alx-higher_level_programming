#!/usr/bin/python3
""" Whats my status with requests """

if __name__ == "__main__":
    import requests
    url = "https://intranet.hbtn.io/status"
    res = requests.get(url)
    body = res.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
