from typing import Final
import requests

API_KEY: Final[str] = '578304812e537deb28c95e2b3aa3963e94f9f'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'


def shorten_link(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    if url_data := data.get('url'):
        try:
            if url_data['status'] == 7:
                short_link: str = url_data['shortLink']
                print(f'Link: {short_link}')
        except Exception as e:
            print('Error Status: ', {e})
        else:
            print('Error status: ',
                  url_data['status'], request.reason)


def main():
    input_link: str = input('Enter a link: ')
    shorten_link(input_link)


if __name__ == '__main__':
    main()
