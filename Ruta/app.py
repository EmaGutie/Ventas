from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import date
from config.db import get_db
from Models.ventas import Venta
from Models.detalle_venta import detalle_venta
from Models.Producto import Producto
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/ventas", tags=["Ventas"])

# Esquemas de entrada
class ProductoVenta(BaseModel):
    producto_id: int
    cantidad: int

class VentaCreate(BaseModel):
    fecha: date
    cliente_id: int
    descuento: float = 0.0
    productos: List[ProductoVenta]

@router.post("/")
def crear_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    total = 0
    detalles = []

    for item in venta.productos:
        producto = db.query(Producto).filter(Producto.id == item.producto_id).first()
        if not producto:
            raise HTTPException(status_code=404, detail=f"Producto ID {item.producto_id} no encontrado")
        if producto.stock < item.cantidad:
            raise HTTPException(status_code=400, detail=f"Stock insuficiente para {producto.nombre}")

        subtotal = producto.precio * item.cantidad
        total += subtotal

        detalle = detalle_venta(
            producto_id=producto.id,
            cantidad=item.cantidad,
            precio_unitario=producto.precio,
            subtotal=subtotal
        )
        detalles.append(detalle)

        producto.stock -= item.cantidad

    total_con_descuento = total * (1 - venta.descuento)

    nueva_venta = Venta(
        fecha=venta.fecha,
        cliente_id=venta.cliente_id,
        descuento=venta.descuento,
        total=total_con_descuento,
        detalles=detalles
    )

    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)

    return {"mensaje": "Venta registrada exitosamente", "venta_id": nueva_venta.id}
