from flask import Flask
from .auth.routes import auth
from .blog.routes import blog

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(blog, url_prefix='/blog')
    
    return app