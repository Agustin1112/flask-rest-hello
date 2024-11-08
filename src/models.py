from flask_sqlalchemy import SQLAlchemy

# Instancia de db
db = SQLAlchemy()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    height = db.Column(db.String(80))
    gender = db.Column(db.String(20))

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'gender': self.gender
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    climate = db.Column(db.String(80))
    terrain = db.Column(db.String(80))

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'terrain': self.terrain
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    favorites = db.relationship('Favorites', backref='user', lazy=True)

    def as_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def as_dict(self):
        return {
            'id': self.id,
            'planet_id': self.planet_id,
            'people_id': self.people_id,
            'user_id': self.user_id
        }
