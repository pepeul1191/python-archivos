#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from config.models import imagenes
from config.database import generator_id
from config.database import generator_id
from config.constants import constants
from tinydb import Query

imagen_view = Bottle()

@imagen_view.route('/crear', method='POST')
def imagen_subir():
	rpta = None
	try:
		imagen = json.loads(request.query.data)
		imagenes.insert(imagen)
		rpta = {'tipo_mensaje' : 'success', 'mensaje' : ['Se ha registrado una nueva imagen', imagen['id']]}
	except TypeError:
		rpta = {'tipo_mensaje' : 'error', 'mensaje' : ['Se ha producido un error en guardar la imagen', str(e)]}	
	return json.dumps(rpta)

@imagen_view.route('/obtener_id', method='GET')
def imagen_obtener_id():
	return generator_id()

@imagen_view.route('/listar', method='GET')
def imagen_listar():
	return json.dumps(imagenes.all())

@imagen_view.route('/obtener_ruta_archivo/<imagen_id>', method='GET')
def imagen_obtener_ruta_archivo(imagen_id):
	Imagen = Query()
	tmp = imagenes.search(Imagen.id == imagen_id)
	rpta = None
	if tmp == []:
		rpta = ''
	else:
		rpta = constants['SERVER_URL'] + tmp[0]['nombre_generado'] 
	return rpta

@imagen_view.route('/obtener_nombre_archivo/<imagen_id>', method='GET')
def imagen_obtener_nombre_archivo(imagen_id):
	Imagen = Query()
	tmp = imagenes.search(Imagen.id == imagen_id)
	rpta = None
	if tmp == []:
		rpta = ''
	else:
		rpta = tmp[0]['nombre_generado'] 
	return rpta