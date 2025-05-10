from flask import Blueprint, request, jsonify
from Models import db,detalle_venta

detalle_bp = Blueprint('productos', __name__, url_prefix='/productos')

@detalle_bp.route('/', methods=['GET'])
def get_detalle_venta():
    deta_venta = detalle_venta.query.all()
    return jsonify([p.to_dict() for p in deta_venta])

@detalle_bp.route('/<int:id>', methods=['GET'])
def get_producto(id):
    producto = detalle_venta.query.get_or_404(id)
    return jsonify(producto.to_dict())

@detalle_bp.route('/', methods=['POST'])
def crear_producto():
    data = request.get_json()
    if not all(k in data for k in ('id_detalle', 'id_productos', 'id_venta','fecha_emitido','hora_emitido')):
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    nuevo = detalle_venta(
        fecha_emitido=data['fecha_emitido'],
        hora_emitido=data['hora_emitido'],
    
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

@detalle_bp.route('/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    deta_venta = detalle_venta.query.get_or_404(id)
    data = request.get_json()

    deta_venta.fecha_emitido= data.get('nombre', deta_venta.fecha_emitido)
    deta_venta.hora_emitido = data.get('precio', deta_venta.hora_emitido)
   

    db.session.commit()
    return jsonify(deta_venta.to_dict())

