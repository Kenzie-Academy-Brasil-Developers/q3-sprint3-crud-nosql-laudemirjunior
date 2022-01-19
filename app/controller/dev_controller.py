from app import db
from flask import jsonify

def get_posts():
    data_list = db.posts.find()
    data_list = list(data_list)
    data_list = del_id(data_list)
    return jsonify(data_list)

def create_new_post(data_list):
    db.posts.insert_one(data_list.__dict__)
    del data_list.__dict__["_id"]
    return create_new_post

def del_post(id):
    data_list = db.posts.find_one({"id": id})
    db.posts.delete_one(data_list)
    del data_list["_id"]
    return jsonify(data_list), 200

def del_id(data_list):
    posts = []
    for post in data_list:
        del post["_id"]
        posts.append(post)
    return posts

def len_posts():
    data_list = db.posts.find()
    data_list = list(data_list)
    return len(data_list)

def verify_keys_for_edit(data):
    trusted_keys = ["title", "author", "tags", "content"]
    for key in data:
        if not key in trusted_keys:
            raise KeyError
