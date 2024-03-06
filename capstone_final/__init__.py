from flask import Flask
from flask_migrate import Migrate


from .blueprints.site.routes import site
from .blueprints.auth.routes import auth
from config import Config
from .models import login_manager, db

app = Flask(__name__)

app.config.from_object(Config)

login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in'
login_manager.login_message = "Log in to access your account!"
login_manager.login_message_category = 'warning'


app.register_blueprint(site)
app.register_blueprint(auth)


db.init_app(app)
migrate = Migrate(app, db)

