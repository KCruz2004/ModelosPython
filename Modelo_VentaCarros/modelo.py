from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base= declarative_base()

class Venta(Base):
    __tablename__ = 'tbl_venta'
    
    id=Column(Integer, primary_key=True)
    nombre_venta=Column(String, nullable= False)
    
    cliente=relationship("Cliente", back_populates="clientes")
    carro=relationship("Carro", back_populates="carro")
    
class Cliente(Base):
    __tablename__ ='tbl_cliente'
    
    id=Column(Integer, primary_key=True)
    nombre_cliente=Column(String, nullable=False)
    ventas_id=Column(Integer, ForeignKey('tbl_venta.id'))
    
    venta=relationship("Venta", back_populates="venta")
    carro= relationship("Carro", back_populates="carro")
    
class Carro(Base):
    __tablename__ ='tbl_carro'
    
    id=Column(Integer, primary_key=True)
    nombre_carro= Column(String, nullable=False)
    venta_id=Column(Integer, ForeignKey('tbl_venta.id'))
    
    venta=relationship("Venta", back_populates="venta")
    realizar_venta= relationship("RealizarVenta", back_populates="vender")
    
class RealizarVenta(Base):
    __tablename__ ='tbl_ventas'
    id= Column(Integer, primary_key=True)
    
    carro_id= Column(Integer,ForeignKey('tbl_carro.id'))
    cliente_id=Column(Integer, ForeignKey('tbl_cliente.id'))
    
    carro= relationship("Carro", back_populates="carro")
    cliente= relationship("Cliente", back_populates="cliente")
    
engine=create_engine('sqlite:///ventacarro.db', echo=True)

Base.metadata.create_all(engine)
