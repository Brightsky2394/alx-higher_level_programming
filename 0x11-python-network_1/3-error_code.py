#!/usr/bin/python3
""" Error code """

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys
    url = sys.argv[1]
    try:
        with urlopen(url) as res:
            body = res.read().decode('utf-8')
            print(body)

    except HTTPError as err:
        print('Error code: {}'.format(err.code))
