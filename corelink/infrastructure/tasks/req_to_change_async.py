from celery import shared_task
from typing import Union


@shared_task
def set_request_to_change(user_id:int,wiki_id:int,title:Union[str,None],text:Union[str,None]):
    print("Вызвался таск")
    from domain.services.wiki_service.wiki_change_service import RequestToChangeWiki
    return RequestToChangeWiki(user_id).SET_REQUEST_TO_CHANGE(wiki_id=wiki_id,title=title,text=text)

@shared_task
def accept_request_to_change(user_id,request_id):
    from domain.services.wiki_service.wiki_change_service import RequestToChangeWiki
    return RequestToChangeWiki(user_id=user_id).ACCEPT_REQUEST_CHANGE(request_id)
@shared_task 
def delete_request_change(user_id,request_id):
    from domain.services.wiki_service.wiki_change_service import RequestToChangeWiki
    return RequestToChangeWiki(user_id).DELETE_REQUEST_CHANGE(request_id)