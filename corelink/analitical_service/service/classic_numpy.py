import numpy as np
from infrastructure.db.repositories.user_repository import UserRepository,User
from infrastructure.db.wiki_repositories.crud import WikiRepository,Wiki
import numpy as np

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