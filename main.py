import requests
import json


def write_json(data, friends, id):
    with open(f'{id}.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    with open(f'{id}.json', 'a') as file:
        json.dump(friends, file, indent=2, ensure_ascii=False)


def main():
    api_version = 5.154
    id = input('Please input VK user ID: ')  # ID человека для запроса, пример: a_gamilkar или 2974856
    access_token = '853b8233853b8233853b82330e862e79a98853b853b8233e01607bc929e59a68a44dce1'  # Токен для запросов, получаем при создание Standalone приложение ВК.

    person_req = requests.get(f'https://api.vk.com/method/users.get?user_ids={id}&v=5.154&access_token={access_token}')
    friends_req = requests.get(f'https://api.vk.com/method/users.getFollowers?user_id=1&fields=city,country&count=100&offset={1}&access_token={access_token}&v={api_version}')

    friends = []
    for friend in friends_req.json()["response"]['items']:
        friends.append(friend["last_name"])

    slovar={}
    slovar["friends"] = friends

    write_json(person_req.json(), json.dumps(slovar), id)


if __name__ == '__main__':
    main()





