from infrastructure.cache.users_top_by_likes import UserTop_toCache
from infrastructure.tasks.beat_users_top_by_likes import set_top_users_by_likes
import pandas
def get_data():
    users_list:list[dict] = UserTop_toCache().GET_DATA()
    for user in users_list:
        print(user)
        print("")
    # print(users_list)
    df = pandas.DataFrame(users_list)
    df_sorted = df.sort_values(by="likes_count",ascending=False)
    df_list_dict = df_sorted.to_dict(orient="records")
    print(df_sorted)
    return df_list_dict
def set_data():
    set_top_users_by_likes.delay()
    return True