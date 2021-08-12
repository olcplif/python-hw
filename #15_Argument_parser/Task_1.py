# 1. Написати програму яка буде зберігати username і email в файл json.
# При наявності користувачів перед тим як додати юзера програма повинна перевірити чи не існує на данний момент
# користувача з таким username і email, якщо існує вивести помилку.

import argparse
import json


class ParsErrorUsername(Exception):
    pass


class ParsErrorEmail(Exception):
    pass


parser = argparse.ArgumentParser()

parser.add_argument("--username", help="Enter username")
parser.add_argument("--email", help="Enter email")
args = parser.parse_args()
user_dict = {}

if args.username:
    user_dict['username'] = args.username

if args.email:
    user_dict['email'] = args.email

user_file = open('users.json', 'r')
users_data = json.loads(user_file.readline())
user_file.close()

# TODO: Maybe to use the function

try:
    for user in users_data:
        if user['username'] == user_dict['username']:
            raise ParsErrorUsername
        elif user['email'] == user_dict['email']:
            raise ParsErrorEmail

    users_data.append(user_dict)

except ParsErrorUsername:
    print("Such a username is present")
except ParsErrorEmail:
    print("Such a email is present")

user_file = open('users.json', 'w')
user_file.write(json.dumps(users_data))
user_file.close()
