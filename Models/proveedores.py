from Models.db import db

class Proveedores(db.Model):
    
    __tablename__ = 'Proveedores'
    id_Proveedor = db.column(db.Integer, Primary_Key=True)
    Nombre_Proveedor = db.column(db.String(100), nullable=False)
    Telefono = db.column(db.Integer,unique=True,nullable=False)
    E_mail_Proveedor = db.column(db.Itring(150),unique=True,nullable=False)

    def __init__(self,id_Proveedor,Nombre_Proveedor,Telefono,E_mail_Proveedor):
        self.id_Proveedor=id_Proveedor
        self.Nombre_Proveedor=Nombre_Proveedor
        self.Telefono=Telefono
        self.E_mail_Proveedor=E_mail_Proveedor

    def serialize(self):
        return{'id_Proveedor':self.id_Proveedor,
               'Nombre_Proveedor':self.Nombre_Proveedor,
               'Telefono':self.Telefono,
               'E_mail_Proveedor':self.E_mail_Proveedor
            
        }