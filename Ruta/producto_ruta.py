from flask import Blueprint, request, jsonify
from Models import db,Producto

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([p.to_dict() for p in productos])

@productos_bp.route('/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify(producto.to_dict())

@productos_bp.route('/', methods=['POST'])
def crear_producto():
    data = request.get_json()
    if not all(k in data for k in ('nombre', 'precio', 'fecha_ingreso')):
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    nuevo = Producto(
        nombre=data['nombre'],
        precio=data['precio'],
        fecha_ingreso=data['fecha_ingreso'],
        descripcion=data.get('descripcion', '')
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

@productos_bp.route('/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = Producto.query.get_or_404(id)
    data = request.get_json()

    producto.nombre = data.get('nombre', producto.nombre)
    producto.precio = data.get('precio', producto.precio)
    producto.fecha_ingreso = data.get('fecha_ingreso', producto.fecha_ingreso)
    producto.descripcion = data.get('descripcion', producto.descripcion)

    db.session.commit()
    return jsonify(producto.to_dict())

@productos_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({'mensaje': 'Producto eliminado'})