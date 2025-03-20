from flask import Flask
from config import Config
from extensions import db, ma, migrate
from controllers.item_controller import item_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(item_bp, url_prefix="/api/items")