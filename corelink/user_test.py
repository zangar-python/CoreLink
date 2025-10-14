import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'corelink.settings')  # имя твоего settings
django.setup()

from domain.services.user_auth import UserAuth_Log
from domain.services.admin_func import Admin_class_func
from infrastructure.db.repositories.user_repository import UserRepository
from infrastructure.db.wiki_repositories.crud import WikiRepository

import pandas

admin = UserRepository().get_user(id=4)

usernames = []
titles = []
user_ids = []
activity = []

if admin:
    print(admin)
for i in range(1,10):
    res = UserAuth_Log().user_register(
        username=f"test-user{i}",
        password=f"1234pass",
        email=f"test-email{i}"
    )
    # user = res['data']['user']
    # print(res)
    # WikiRepository()

print("DELETE PROCESS")
# for i in range(1,10):
#     # print(f"cicle for {i}")
#     # res = UserAuth_Log().get_user_by(username=f"test-user{i}")
    
#     # if res['is_error']:
#     #     print("Пользователь не найден")
#     #     continue
#     # user = res['data']['user']
#     user = UserRepository().get_user(username=f"test-user{i}")
#     if not user:
#         print("NOT FOUNDED")
#         continue
#     # print(user.username,user.id)
#     wiki = WikiRepository(user).create_wiki(
#         title=f"title {i} of user {user.username}",
#         text=f"text {i} of this wiki"
#     )
#     # print(wiki.title,wiki.text,wiki.id)
#     usernames.append(user.username)
#     titles.append(wiki.title)
#     user_ids.append(user.id)
#     activity.append(user.activity.active)
    
#     Admin_class_func().delete_user(admin,user.id)
# print("TEST USERS DELETED")

# df = pandas.DataFrame({
#     "username":usernames,
#     "title":titles,
#     "user_id":user_ids,
#     "activity":activity
# })
# print(df)

