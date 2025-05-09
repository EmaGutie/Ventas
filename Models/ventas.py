from Models.db import db

class Ventas(db.Model):

    __tablename__ = 'Ventas'

    id_venta = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    id_cliente = db.Column(db.Integer, nullable=False)
    id_vendedor = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, id_venta, fecha, id_cliente, id_vendedor, total):
        self.id_venta = id_venta
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.id_vendedor = id_vendedor
        self.total = total

    def serialize(self):
        return {
            'id_venta': self.id_venta,
            'fecha': self.fecha.isoformat(),  # convierte fecha a string 
            'id_cliente': self.id_cliente,
            'id_vendedor': self.id_vendedor,
            'total': self.total
        }
