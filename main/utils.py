import json


class PostHandler:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        with open(self.path,  encoding='utf-8') as file:
            posts = json.load(file)
        return posts

    def search_posts(self, substr):
        new_posts = []
        load_posts = self.load_posts()
        for post in load_posts():
            if substr.lower() in post['content'].lower():
                new_posts.append(post)
        return new_posts



