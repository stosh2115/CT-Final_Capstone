from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from datetime import datetime
import uuid
from flask_marshmallow import Marshmallow

from .helpers import get_image

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    user_id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    gender = db.Column(db.String(30))
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, username, gender, email, password, first_name="", last_name=""):
        self.user_id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_id(self):
        return str(uuid.uuid4())
    
    def get_id(self):
        return str(self.user_id)
    
    def set_password(self, password):
        return generate_password_hash(password)
    
    def __repr__(self): 
        return f"<User: {self.username}>"


class Venues(db.Model):
    ven_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    location = db.Column(db.String(150))
    demographics = db.Column(db.Integer)
    image = db.Column(db.String)

    def __init__(self, name, city, state, location, demographics, image=""):
        self.ven_id = self.set_id()
        self.name = name
        self.city = city
        self.state = state
        self.location = location
        self.demographics = demographics
        self.image = self.set_image(image,name)



    def set_id(self):
        return str(uuid.uuid4())
    
    
    def set_image(self, image, name):
        
        if not image:
            image = get_image(name) 
        
        return image

    


class ProductSchema(ma.Schema):

    class Meta: 
        fields = ['ven_id', 'name', 'location', 'image']


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


