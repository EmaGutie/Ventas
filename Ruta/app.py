from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from Models.db import db
from Models.Cliente import Cliente
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Crear cliente
@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    nuevo = Cliente(nombre=data['nombre'], telefono=data['telefono'], e_mail=data['e_mail'])
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.serialize()), 201

# Obtener todos
@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    clientes = Cliente.query.all()
    return jsonify([c.serialize() for c in clientes])

# Obtener uno
@app.route('/clientes/<int:id>', methods=['GET'])
def obtener_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.serialize())

# Actualizar
@app.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    data = request.json
    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.telefono = data.get('telefono', cliente.telefono)
    cliente.e_mail = data.get('e_mail', cliente.e_mail)
    db.session.commit()
    return jsonify(cliente.serialize())

# Eliminar
@app.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente eliminado'})

if __name__ == '__main__':
    app.run(debug=True)
# ---------------------------Cliente-Crud-------------------------------------------
