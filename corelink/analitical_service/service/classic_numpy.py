import numpy as np
from infrastructure.db.repositories.user_repository import UserRepository,User
from infrastructure.db.wiki_repositories.crud import WikiRepository,Wiki
import pandas as pd

def numpy_classis_analitics(list):
    arr = np.array(list)
    
    
    return {
        "max":float(arr.max()),
        "min":float(arr.min()),
        "mean":float(arr.mean()),
        "count":arr.size,
        "sum":float(arr.sum())
    }

def get_users_wiki_likes():    
    users_wiki_likes = Wiki.objects.prefetch_related("likes")
    users = []
    for wiki in users_wiki_likes:
        users.append(wiki.likes.all().values_list("id",flat=True))
    return users
import pandas as pd
import numpy as np

def get_users(target_id=96):
    users = User.objects.prefetch_related("likes")

    # Формируем DataFrame
    data = []
    for user in users:
        likes_ids = list(user.likes.values_list("id", flat=True))
        data.append({"user_id": user.pk, "likes": set(likes_ids)})

    df = pd.DataFrame(data)

    # Лайки целевого пользователя
    target_likes = df.loc[df["user_id"] == target_id, "likes"].iloc[0]

    # Считаем похожесть (Жаккар)
    def jaccard(a, b):
        inter = len(a & b)  # пересечение
        union = len(a | b)  # объединение
        return inter / union if union != 0 else 0

    df["similarity"] = df["likes"].apply(lambda x: jaccard(x, target_likes))

    # Отсортируем по убыванию похожести (и исключим самого пользователя)
    similar = df[df["user_id"] != target_id].sort_values("similarity", ascending=False)

    return similar

def user_likes_recomends(user_id):
    users = User.objects.prefetch_related("likes").all().values_list("id","likes__id")
    user = list(users.filter(id=user_id))
    # print(users)
    # print(user)
    # user_id = user.id
    # user_likes = user.likes__id
    users_likes = []
    users_id = []
    print(user)
    
    users = []
    
    for u in users:
        users_likes.append(u[1])
        users_id.append(u[0])
    for u in range(len(users_id)):
        if not users_likes[u]:
            users_likes[u] = 0
        print(users_id[u],users_likes[u])
    # print(user_likes)    
    
    return True
    
        