import json
from json import JSONDecodeError

class PostHandler:
    def __init__(self, path):
        self.path = path

    def load_posts(self):
        posts = []
        load_posts = self.load_posts()
        try:
            with open(self.path,  encoding='utf-8') as file:
                posts = json.load(file)
        except JSONDecodeError:
                return posts, 'Ошибка получения данных из JSON'


        return posts, None

    def search_posts(self, substr):
        new_posts = []
        load_posts, error = self.load_posts()

        for post in load_posts:
            if substr.lower() in post['content'].lower():
                new_posts.append(post)

        return new_posts, error
    def save_posts_to_json(self, posts):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(posts, file)

    def add_post(self, post):
        posts, error = self.load_posts()
        posts.append(post)
        self.save_posts_to_json(posts)






