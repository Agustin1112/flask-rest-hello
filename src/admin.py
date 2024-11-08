from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, People, Planets, User, Favorites
from app import app

# Creo la instancia de Admin
admin = Admin(app, name='StarWars Blog Admin', template_mode='bootstrap3')

# Añado vistas de los modelos al admin
admin.add_view(ModelView(People, db.session))
admin.add_view(ModelView(Planets, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Favorites, db.session))
