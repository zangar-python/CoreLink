
from celery import shared_task


@shared_task
def set_top_users_by_likes():
    from infrastructure.cache.users_top_by_likes import UserTop_toCache
    from domain.services.user_rating.service import UserRatingService,User
    
    admin = User.objects.get(id=4)
    user_service = UserRatingService(admin)
    
    users = user_service.get_users()
    sorted_users = user_service.sort_users(users)
    UserTop_toCache().SET_DATA(sorted_users)
    return
