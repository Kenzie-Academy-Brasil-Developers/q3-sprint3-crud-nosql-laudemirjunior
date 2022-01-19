from app.controller.dev_controller import len_posts
from datetime import datetime

class Post():
    def __init__(self, title, author, tags, content):
        self.id = len_posts() + 1
        self.created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.updated_at = None
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content