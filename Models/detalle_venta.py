from Models.db import db
class detalle_venta(db):
    __tablename__="detalle_venta"
    id_detalle= db.column(db.Integer(), primary_key=True),
    id_productos=db.column(db.integer(), db.foreignkey('productos.id'), nullable=False)
    id_venta=db.column(db.integer(),db.foreingkey('ventas.id'), nullable=False)
    fecha_emitido=db.column(db.Date(),nullable=False)
    hora_emitido=db.column(db.date(),nullable=False)
    def __init__(self,id_detalle,id_productos,id_venta,fecha_emitido,hora_emitido):
        self.id_detalle=id_detalle
        self.id_productos=id_productos
        self.fecha_emitido=fecha_emitido
        self.hora_emitido=hora_emitido
    def to_dict(self) :
        return{
            'id_detalle': self.id_detalle,
            'id_producto':self.id_productos,
            'id_venta':self.id_venta,
            'feche_emitido':self.fecha_emitido,
            'hora_emitido':self.hora_emitido
        }   
