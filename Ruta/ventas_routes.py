from flask import Flask, request, jsonify
from Models.db import db
from Models.ventas import Ventas
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Crear venta
@app.route('/ventas', methods=['POST'])
def create_venta():
    data = request.get_json()
    nueva_venta = Ventas(
        id_venta=data['id_venta'],
        fecha=data['fecha'],
        id_cliente=data['id_cliente'],
        id_vendedor=data['id_vendedor'],
        total=data['total']
    )
    db.session.add(nueva_venta)
    db.session.commit()
    return jsonify(nueva_venta.serialize()), 201

# Obtener todas las ventas
@app.route('/ventas', methods=['GET'])
def get_ventas():
    ventas = Ventas.query.all()
    return jsonify([v.serialize() for v in ventas]), 200

# Obtener venta por ID
@app.route('/ventas/<int:id_venta>', methods=['GET'])
def get_venta(id_venta):
    venta = Ventas.query.get_or_404(id_venta)
    return jsonify(venta.serialize())

# Actualizar venta
@app.route('/ventas/<int:id_venta>', methods=['PUT'])
def update_venta(id_venta):
    venta = Ventas.query.get_or_404(id_venta)
    data = request.get_json()
    venta.fecha = data['fecha']
    venta.id_cliente = data['id_cliente']
    venta.id_vendedor = data['id_vendedor']
    venta.total = data['total']
    db.session.commit()
    return jsonify(venta.serialize())

# Eliminar venta
@app.route('/ventas/<int:id_venta>', methods=['DELETE'])
def delete_venta(id_venta):
    venta = Ventas.query.get_or_404(id_venta)
    db.session.delete(venta)
    db.session.commit()
    return jsonify({'message': 'Venta eliminada'})

if __name__ == '__main__':
    app.run(debug=True)
