from flask import Flask

def init_app(app: Flask):
    from app.routes.dev_route import posts_view
    posts_view(app)