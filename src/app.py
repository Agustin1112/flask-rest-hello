from flask import Flask, jsonify
from models import db, People, Planets, User, Favorites
from utils import create_app

# Creo la aplicación utilizando la función desde utils.py
app = create_app()

@app.route('/')
def index():
    return "¡Bienvenido al Star Wars Blog API!"

# Endpoints para personas
@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify([person.as_dict() for person in people])

@app.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    person = People.query.get_or_404(people_id)
    return jsonify(person.as_dict())

# Endpoints para planetas
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    return jsonify([planet.as_dict() for planet in planets])

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get_or_404(planet_id)
    return jsonify(planet.as_dict())

# Endpoints para usuarios
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.as_dict() for user in users])

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    user = User.query.first()  #  Usuario autenticado
    favorites = Favorites.query.filter_by(user_id=user.id).all()
    return jsonify([favorite.as_dict() for favorite in favorites])

# Endpoints para agregar favoritos
@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user = User.query.first()  #  Usuario autenticado
    planet = Planets.query.get_or_404(planet_id)
    new_favorite = Favorites(user_id=user.id, planet_id=planet.id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(new_favorite.as_dict()), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    user = User.query.first()  # Usuario autenticado
    person = People.query.get_or_404(people_id)
    new_favorite = Favorites(user_id=user.id, people_id=person.id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(new_favorite.as_dict()), 201

# Endpoints para eliminar favoritos
@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user = User.query.first()  # Usuario autenticado
    favorite = Favorites.query.filter_by(user_id=user.id, planet_id=planet_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return '', 204
    return jsonify({'message': 'Favorite not found'}), 404

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    user = User.query.first()  # Usuario autenticado
    favorite = Favorites.query.filter_by(user_id=user.id, people_id=people_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        return '', 204
    return jsonify({'message': 'Favorite not found'}), 404

