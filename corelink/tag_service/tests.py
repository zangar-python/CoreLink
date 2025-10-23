from django.test import TestCase

from .services.repo_tag import Tag_Wiki_Repo
from infrastructure.db.wiki_repositories.crud import WikiRepository
from infrastructure.db.repositories.user_repository import UserRepository
# Create your tests here.

class Test_tag_model(TestCase):
    def test_tag_info(self):
        first_user = UserRepository().create_user("Test-user-tag","test_1234","test-email@gmail.com")
        wiki_repo = WikiRepository(first_user)
        first_wiki = wiki_repo.create_wiki("test wiki","Test Test Test Test")
        tag_repo = Tag_Wiki_Repo()
        test_tags_name = [
            "test_tag1",
            "test_tag2",
            "test_tag3",
            "test_tag4",
        ]
        
        if tag_repo.add_tags(first_wiki,test_tags_name):
            tags = tag_repo.get_wiki_tags(first_wiki)
            
            
            for tag in tags:
                tag_info = tag_repo.get_tag_info(tag)
                tag_repo.delete_tag(pk=tag.pk)