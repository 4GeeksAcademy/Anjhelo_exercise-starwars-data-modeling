import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

    
class Peliculas(Base):
    __tablename__ = "peliculas"
    Id_peliculas = Column(String(6), primary_key=True)
    Titulo = Column(String(100))
    Director = Column(String(100))
    personajes = relationship("Personajes", secondary="peliculas_personajes")

class Personajes(Base):
    __tablename__ = "personajes"
    Id_Personajes = Column(String(6), primary_key=True)
    Nombre = Column(String(100))
    Genero = Column(String(30))
    Altura = Column(String(5))
    Peso = Column(String(5))
    Color_pelo = Column(String(12))
    Color_ojos = Column(String(12))
    Color_piel = Column(String(12))
    planeta = relationship("Planetas", secondary="planetas_personajes")
    naves = relationship("Naves", secondary="personajes_naves")
    vehiculos = relationship("Vehiculos", secondary="personajes_vehiculos")
    peliculas = relationship("Peliculas", secondary="peliculas_personajes")
    especie_id = Column(String(6), ForeignKey('especies.Id_especie'))
    especie = relationship("Especies")

class Planetas(Base):
    __tablename__ = "planetas"
    Id_planeta = Column(String(6), primary_key=True)
    Nombre = Column(String(30))
    Poblacion = Column(Integer)
    Clima = Column(String(10))
    Gravedad = Column(String(10))
    personajes = relationship("Personajes", secondary="planetas_personajes")

class Especies(Base):
    __tablename__ = "especies"
    Id_especie = Column(String(6), primary_key=True)
    Nombre = Column(String(30))
    Claseficación = Column(String(30))
    Lenguaje = Column(String(30))
    Vida_estimada = Column(Integer)
    Color_pelo = Column(String(12))
    Color_ojos = Column(String(12))
    Color_piel = Column(String(12))
    personajes = relationship("Personajes")

class Naves(Base):
    __tablename__ = "naves"
    Id_nave = Column(String(6), primary_key=True)
    Nombre = Column(String(30))
    Modelo = Column(String(40))
    Clase = Column(String(20))
    Fabricante = Column(String(35))
    Costo = Column(Integer)
    Carga = Column(Integer)
    Pasajeros = Column(Integer)
    personajes = relationship("Personajes", secondary="personajes_naves")

class Vehiculos(Base):
    __tablename__ = "vehiculos"
    Id_vehiculo = Column(String(6), primary_key=True)
    Nombre = Column(String(30))
    Modelo = Column(String(30))
    Clase = Column(String(20))
    Fabricante = Column(String(35))
    Costo = Column(Integer)
    Carga = Column(Integer)
    Pasajeros = Column(Integer)
    personajes = relationship("Personajes", secondary="personajes_vehiculos")

class Usuarios(Base):
    __tablename__ = "usuarios"
    Id_usuario = Column(String(6), primary_key=True)
    Nombre = Column(String(100))
    email = Column(String(100), unique=True)
    favoritos = relationship("Favoritos", secondary="usuarios_favoritos")

class Favoritos(Base):
    __tablename__ = "favoritos"
    Id_favorito = Column(String(6), primary_key=True)
    planeta_id = Column(String(6), ForeignKey('planetas.Id_planeta'), nullable=True)
    nave_id = Column(String(6), ForeignKey('naves.Id_nave'), nullable=True)
    personaje_id = Column(String(6), ForeignKey('personajes.Id_Personajes'), nullable=True)
    usuarios = relationship("Usuarios", secondary="usuarios_favoritos")

class PeliculasPersonajes(Base):
    __tablename__ = "peliculas_personajes"
    pelicula_id = Column(String(6), ForeignKey('peliculas.Id_peliculas'), primary_key=True)
    personaje_id = Column(String(6), ForeignKey('personajes.Id_Personajes'), primary_key=True)

class PlanetasPersonajes(Base):
    __tablename__ = "planetas_personajes"
    planeta_id = Column(String(6), ForeignKey('planetas.Id_planeta'), primary_key=True)
    personaje_id = Column(String(6), ForeignKey('personajes.Id_Personajes'), primary_key=True)

class PersonajesNaves(Base):
    __tablename__ = "personajes_naves"
    personaje_id = Column(String(6), ForeignKey('personajes.Id_Personajes'), primary_key=True)
    nave_id = Column(String(6), ForeignKey('naves.Id_nave'), primary_key=True)

class PersonajesVehiculos(Base):
    __tablename__ = "personajes_vehiculos"
    personaje_id = Column(String(6), ForeignKey('personajes.Id_Personajes'), primary_key=True)
    vehiculo_id = Column(String(6), ForeignKey('vehiculos.Id_vehiculo'), primary_key=True)

class UsuariosFavoritos(Base):
    __tablename__ = "usuarios_favoritos"
    usuario_id = Column(String(6), ForeignKey('usuarios.Id_usuario'), primary_key=True)
    favorito_id = Column(String(6), ForeignKey('favoritos.Id_favorito'), primary_key=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
