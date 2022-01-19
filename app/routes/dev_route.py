from app.controller.dev_controller import create_new_post, del_id, get_posts, verify_keys_for_edit
from app.controller.dev_decorators import verify_keys
from flask  import Flask, jsonify, request
from app.model.dev_model import Post
from datetime import datetime
from app import db

def posts_view(app: Flask):

    @app.get('/posts')
    def read_posts():
        return get_posts(), 200

    @app.post('/posts')
    @verify_keys()
    def create_post():
        data_list = Post(**request.get_json())
        create_new_post(data_list)
        return jsonify(data_list.__dict__), 201

    @app.get('/posts/<int:id>')
    def read_post_by_id(id):
        try:
            data_list = db.posts.find_one({"id": id})
            del data_list["_id"]
            return jsonify(data_list), 200
        except TypeError: 
            return jsonify(msg= "Post buscado não existe"), 404

    @app.delete('/posts/<int:id>')
    def delete_post(id):
        try:
            data_list = db.posts.find_one({"id": id})
            db.posts.delete_one(data_list)
            del data_list["_id"]
            return jsonify(data_list), 202
            
        except TypeError: 
            return jsonify(msg= "Post buscado não existe"), 404
    
    @app.patch('/posts/<int:id>')
    def update_post(id):
        try:
            verify_keys_for_edit(request.get_json())

            db.posts.update_one({"id": id}, {"$set": {**request.get_json(), "updated_at": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}})

            data_list = db.posts.find_one({"id": id})
            del data_list["_id"]
            return jsonify(data_list), 200
        except KeyError:
            return jsonify(msg="Valor(es) incorreto(s)"), 400
        except TypeError:
            return jsonify(msg= "Post buscado não existe"), 404

            

