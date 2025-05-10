from Models.db import db

class user(db.model):
    __tablename__="productos"
    id_productos=  db.column(db.Integer, Primary_Key=True)
    nombre= db.column(db.String(100), nullable=False)
    precio=db.column(db.Integer,nullable=False)
    id_provedor=db.column(db.Integer,foreignkey=True)
    fecha_ingreso= db.Column(db.Date(),nullable=False)
    descripcion= db.Column(db.String(150), nullable=False)
    def __init__(self,id_productos,nombre,precio,id_provedor,fecha_ingreso,descripcion):
        self.id_productos=id_productos
        self.nombre=nombre
        self.precio=precio
        self.id_provedor=id_provedor
        self.fecha_ingreso=fecha_ingreso
        self.descripcion=descripcion
    def to_dict(self):
        return{
            'id_productos':self.id_productos,
            'nombre':self.nombre,
            'precio':self.precio,
            'id_provedor':self.id_provedor,
            'fecha_ingreso':self.fecha_ingreso,
            'descripcion':self.descripcion
            
        }
