import requests
from pprint import pprint

with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()

class VK_user:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }

    def both_friends(self):
        both_friends_url = self.url + 'friends.getMutual'
        both_friends_param = {
            'source_uid': 14869974,
            'target_uid': 492888196
        }
        res = requests.get(both_friends_url, params={**self.params, **both_friends_param})
        res = res.json()
        pprint(res)



user1 = VK_user(token, '5.126')
print(user1.both_friends())
