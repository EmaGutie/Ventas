from flask import Blueprint, request, jsonify
from Models import db
from Models.proveedor import Proveedor

proveedor_bp = Blueprint('proveedores', __name__, url_prefix='/proveedores')

# Obtener todos los proveedores
@proveedor_bp.route('/', methods=['GET'])
def get_proveedores():
    proveedores = Proveedor.query.all()
    return jsonify([p.to_dict() for p in proveedores])

# Obtener un proveedor por ID
@proveedor_bp.route('/<int:id>', methods=['GET'])
def get_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    return jsonify(proveedor.to_dict())

# Crear proveedor
@proveedor_bp.route('/', methods=['POST'])
def crear_proveedor():
    data = request.get_json()
    if not data.get('nombre'):
        return jsonify({'error': 'El nombre es obligatorio'}), 400

    nuevo = Proveedor(
        nombre=data['nombre'],
        direccion=data.get('direccion'),
        telefono=data.get('telefono'),
        email=data.get('email')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

# Actualizar proveedor
@proveedor_bp.route('/<int:id>', methods=['PUT'])
def actualizar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    data = request.get_json()

    proveedor.nombre = data.get('nombre', proveedor.nombre)
    proveedor.direccion = data.get('direccion', proveedor.direccion)
    proveedor.telefono = data.get('telefono', proveedor.telefono)
    proveedor.email = data.get('email', proveedor.email)

    db.session.commit()
    return jsonify(proveedor.to_dict())

# Eliminar proveedor
@proveedor_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_proveedor(id):
    proveedor = Proveedor.query.get_or_404(id)
    db.session.delete(proveedor)
    db.session.commit()
    return jsonify({'mensaje': 'Proveedor eliminado'})
