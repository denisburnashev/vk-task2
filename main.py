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

    def get_friends(self, user_id=None):
        friend_list = []
        if user_id is None:
            user_id = self.owner_id
        friends_url = self.url + 'friends.get'
        friends_param = {
            'count': 500,
            'user_id': user_id,
            'fields': 'nickname'
        }
        res = requests.get(friends_url, params={**self.params, **friends_param})
        res = res.json()
        friends_list = res['response']['items']
        for friend in friends_list:
            friend_list.append(friend)
        return friend_list

    def __and__(self, other_user):
        user1_input = input('Введите id 1 пользователя:\n')
        user1 = other_user.get_friends(user1_input)
        user2_input = input('Введите id 2 пользователя:\n')
        user2 = other_user.get_friends(user2_input)
        print('Общие друзья:')
        for friend_user1 in user1:
            for friend_user2 in user2:
                if friend_user1['id'] == friend_user2['id']:
                    print('Фамилия, Имя:', friend_user1['last_name'], friend_user1['first_name'], 'id пользователя:', friend_user1['id'])




user1 = VK_user(token, '5.126')
user2 = VK_user(token, '5.126')

user1 & user2
