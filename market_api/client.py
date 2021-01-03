import requests

class Client():
    base_url = 'https://marketweb-eu.blackdesertonline.com/'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }

    cookies = {
        'ASP.NET_SessionId': None,
        '__RequestVerificationToken': None,
    }

    data = {
      '__RequestVerificationToken': None,
      'keyType' : '0',
      'subKey'  : '0', #Grade of the item. 0 is +0, 1 is +1 (or Pri for accessories)
      'isUp'    : 'true',
      'mainKey' : None,
    }

    def __init__(self, session_id, cookie_token, form_token):
        self.http = requests.session()

        self.cookies['ASP.NET_SessionId'] = session_id
        self.cookies['__RequestVerificationToken'] = cookie_token
        self.data['__RequestVerificationToken'] = form_token

    def set_item(self, item_id):
        self.data['mainKey'] = item_id

    def set_main_category(self, category_id):
        self.data['mainCategory'] = category_id

    def set_sub_category(self, category_id):
        self.data['subCategory'] = category_id

    def connect(self, method = None):

        try:
            request = self.http.post(
                self.base_url + str(method),
                cookies = self.cookies,
                headers = self.headers,
                data = self.data
                )

        except requests.exceptions.ConnectionError:
            print('Connection Refused')
            return

        if request.status_code == 200:
            if request.text:
                data = request.json()
                error = data.get('error')
                if not error:
                    return data
        else:
            print('Bad Request for url: {}.'.format(request.url))

