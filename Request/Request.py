import json

import requests

from utilities import settings
from utilities.DriverWrapper import DriverWrapper


class Request:

    def __init__(self):
        self.driver = DriverWrapper.get_webdriver()
        base_host = settings.base_host
        self.host = base_host
        self.origin = 'https://' + self.host
        self.requested_url = self.origin

    # def authorization_by_request(self, user_login, user_password):
    #     post_headers = {
    #         'accept': '*/*',
    #         'accept - encoding': 'gzip, deflate, br',
    #         'accept - language': 'ru - RU, ru; q = 0.9, en - US; q = 0.8, en; q = 0.7',
    #         'content - length': '1031',
    #         'content - type': 'multipart/form-data; boundary=----WebKitFormBoundary9cF5qOb6w1BS2wS1',
    #         'origin': 'http://my.newsilpo.iir.fozzy.lan',
    #         'referer': 'https://my.newsilpo.iir.fozzy.lan / login',
    #         'user - agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    #                         ' Chrome/70.0.3538.77 Safari/537.36',
    #     }
    #
    #     body = {
    #         'query': '''mutation login($barcode: String!, $password: String!) {
    #             login(barcode: $barcode, password: $password) {
    #                accessToken {
    #                  ...AccessTokenFragment
    #                  __typename
    #                 }
    #                 user {
    #                   ...UserFragment
    #                   __typename
    #                 }
    #                   __typename
    #             }
    #         }
    #
    #         fragment AccessTokenFragment on  AccessTokenType {
    #           accessToken
    #           expiresAt
    #           __typename
    #         }
    #
    #         fragment UserFragment on User {
    #           id
    #           firstName
    #           lastName
    #           middleName
    #           email
    #           emailConfirmed
    #           notification
    #           barcode
    #           bonusAmount
    #           vouchersAmount
    #           spawnNextCouponDate
    #           __typename
    #         }''',
    #         'variables': {"barcode": '029' + user_login, "password": user_password, "ckey": ""},
    #         'debugName': "",
    #         'operationName': 'login'
    #     }

        # try:
        #     print("{}/graphql".format(self.requested_url))
        #     print(body)
        #     response = requests.post("{}/graphql".format(self.requested_url),
        #                              data=json.dumps(body), headers=post_headers, verify=False)
        #     print('-----Type body in response-----\n' + str(type(body)))
        #     print('-----Response status cods-----\n' + str(response.status_code))
        #     print('-----Response text-----\n' + str(response.text))
        #     print('-----Type response-----\n' + str(type(response)))
        #     if response.status_code is not 200:
        #         raise Exception
        #
        #     token = response.json()['data']['login']['accessToken']['accessToken']
        #     expires_at = response.json()['data']['login']['accessToken']['expiresAt']
        #     print(token)
        #     print(expires_at)
        #
        #     # cookies = response.headers['Set-Cookie']
        #     # session_id = cookies.split(';')[0].split("=")[1]
        #     # expires = cookies.split(';')(2).split("=")[1]
        #     # date_expiration = datetime.strptime(expires, '%a, %d-%b-%Y %H:%M:%S %Z')
        #     expires_dict = {
        #         'domain': '.newsilpo.iir.fozzy.lan',
        #         'name': 'expiresAt',
        #         'path': '/',
        #         'value': expires_at,
        #     }
        #     access_dict = {
        #         'domain': '.newsilpo.iir.fozzy.lan',
        #         'name': 'accessToken',
        #         'path': '/',
        #         'value': token,
        #     }
        #     self.driver.add_cookie(expires_dict)
        #     self.driver.add_cookie(access_dict)
        # except Exception as error:
        #     raise Exception('Authorization request failed with {}. {}'.format(error, response.text))
