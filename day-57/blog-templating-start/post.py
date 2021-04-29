import requests

class Post:
    def __init__(self):
        self.blog_req = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965")
        self.blog_data = self.blog_req.json()
    
    def get_all_blogs(self):
        return self.blog_data

    def get_blog(self, id):
        for blog in self.blog_data:
            if blog['id'] == int(id):
                return blog
