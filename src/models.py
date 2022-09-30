import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250),nullable=False)
    password= Column(String(50),nullable=False)


class Pokemones(Base):
    __tablename__ = 'pokemones'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=False, nullable=False)
    ataque = Column(String(30), unique=False, nullable=False)
    defensa = Column(String(30), unique=False, nullable=False)
    evoluciones = Column(String(30), unique=False, nullable=False)
    imagene = Column(String(30), unique=False, nullable=False)

class Especies(Base):
    __tablename__="especies"
    id = Column(Integer, primary_key=True)
    especie = Column(String(30), unique=True, nullable=False)
    habilidades = Column(String(30), unique=False, nullable=False)

class Fav_Pokemones(Base):
    __tablename__="fav_pokemones"
    id = Column(Integer, primary_key=True)
    pokemones_id = Column(Integer, ForeignKey('pokemones.id') )
    email =  Column(String(120), ForeignKey('user.email'))
    rel_name = relationship('Pokemones')
    rel_user = relationship('User')

class Fav_Especie(Base):
    __tablename__="fav_especie"
    id = Column(Integer, primary_key=True)
    email =  Column(String(120), ForeignKey('user.email'))
    Especie_especie=Column(String(30),ForeignKey('especies.especie'))
    rel_especie=relationship('Especie')
    rel_user = relationship('User')

class Entrenador(Base):
    __tablename__="entrenador"
    id=Column(Integer,primary_key=True)
    name=Column(String(80),unique=False, nullable=False)
    pokemonPrincipal=Column(String(30),ForeignKey('pokemones.id'))
    rel_na = relationship('Pokemones')



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')