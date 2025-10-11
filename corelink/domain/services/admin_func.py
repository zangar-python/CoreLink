from django.contrib.auth.models import User
from infrastructure.db.repositories.super_user_repo import SuperUserRepository
from infrastructure.db.repositories.user_repository import UserRepository
from infrastructure.tasks.task import active_users_get_delete,top_wiki_in_a_day

import pandas as pd
import numpy as np

class Admin_class_func:
    def __init__(self):
        pass
    def RESULT(self,data,err:bool=False):
        return {
            "data":data,
            "error":err
        }
    def get_users(self,user:User):
        super_user_repo = SuperUserRepository(user)
        if not super_user_repo.user_is_superuser(user):
            return self.RESULT({"err":"Вам не доступна эта команда"},True)
        users = super_user_repo.get_users_join_activity()
        user_name = []
        user_password = []
        user_id = []
        user_email = []
        user_active = []
        user_last = []
        users_ = []
        for user_ in users:
            user_name.append(user_.username)
            user_password.append(user_.password)
            user_email.append(user_.email)
            user_id.append(user_.id)
            user_active.append(user_.activity.active)
            user_last.append(user_.activity.last_active.date())    
            user_data = {
                "username":user_.username,
                "password":user_.password,
                "id":user_.id,
                "email":user_.email,
                "activity":{
                    "active":user_.activity.active,
                    "last_active":user_.activity.last_active.date()
                }
            }
            users_.append(user_data)
        
        df_data = {
            "username":user_name,
            "email":user_email,
            "password":user_password,
            "id":user_id,
            "active":user_active,
            "last_active":user_last
        }    
        
        df = pd.DataFrame(df_data)
        conditions = [
            df["active"] < 30,
            (df["active"] >= 30 ) & (df['active'] < 70),
            df["active"] >=70
        ]
        choices = ['low','medium','high']
            
        df['level'] = np.select(conditions,choices,default="unknown")
        df.sort_values(by="active",ascending=False)
        print(df)
        
        return self.RESULT({
            "users":users_,
        })
    def delete_user(self,user:User,id:int):
        super_user_repo = SuperUserRepository(user)
        user_repo = UserRepository()
        if super_user_repo.user_is_superuser(user):
            return self.RESULT({"err":"Вам не доступна эта команда"},True)
        if not user_repo.user_exists(id=id):
            return self.RESULT("пользователь с таким айди не найден",True)
        user_to_del = user_repo.get_user(id=id)
        super_user_repo.delete_user(user_to_del)
        return self.RESULT({"delete":True,"user_id":user_to_del.id})
    def set_top_wikis(self,user:User):
        super_user_repo = SuperUserRepository(user)
        if not super_user_repo.user_is_superuser():
            return self.RESULT("Вам запрещено текущая команда",True)
        top_wiki_in_a_day.delay()
        return self.RESULT("Запрос принят")
    def delete_all_active(self,user:User):
        super_user_repo = SuperUserRepository(user)
        if not super_user_repo.user_is_superuser():
            return self.RESULT("Вам запрещено текущая команда",True)
        active_users_get_delete.delay()
        return self.RESULT("Ваш запрос принят")