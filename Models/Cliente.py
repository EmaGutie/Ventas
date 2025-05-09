from Models.db import db

class clientes(db.Model):
    
    __tablename__ = 'clientes'
    id_cliente = db.column(db.Integer, Primary_Key=True)
    Nombre = db.column(db.String(100), nullable=False)
    Telefono = db.column(db.Integer,unique=True,nullable=False)
    E_mail = db.column(db.Itring(150),unique=True,nullable=False)

    def __init__(self,id_clientes,nombre,Telefono,E_mail):
        self.id_clientes=id_clientes
        self.nombre=nombre
        self.Telefono=Telefono
        self.E_mail=E_mail

    def serialize(self):
        return{'id_clientes':self.id_clientes,
               'nombre':self.nombre,
               'Telefono':self.Telefono,
               'E_mail':self.E_mail
            
        }