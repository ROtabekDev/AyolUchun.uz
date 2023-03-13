from django.test import TestCase
from django.test import Client

from apps.blog.models import Blog, Category_for_blog

class TestBlogListView(TestCase):

    def setUp(self) -> None:
        self.blog1 = Blog.objects.create(title='1-maqola', slug='1-maqola', author='Otabek', content='1-maqola matni')
        self.blog2 = Blog.objects.create(title='2-maqola', slug='2-maqola', author="Ilhom", content='2-maqola matni')
        self.blog3 = Blog.objects.create(title='3-maqola', slug='3-maqola', author='Samandar', content='3-maqola matni')
        
        self.client = Client()
    
    def test_get_all_blogs(self):
        response = self.client.get('/api/v1/blog/list/')

        data = response.data
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]['title'], "1-maqola")
   

class TestCategoryListView(TestCase):

    def setUp(self) -> None:
        self.category1 = Category_for_blog.objects.create(title='1-toifa', slug='1-toifa')
        self.category1 = Category_for_blog.objects.create(title='2-toifa', slug='2-toifa')
        self.category1 = Category_for_blog.objects.create(title='3-toifa', slug='3-toifa')
        
        self.client = Client()
    
    def test_get_all_blogs(self):
        response = self.client.get('/api/v1/blog/category/list/')

        data = response.data
        
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]['title'], "1-toifa")