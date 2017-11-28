#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from bottle import Bottle, request
from config.models import extensiones
from tinydb import Query

extension_view = Bottle()

@extension_view.route('/extension/obtener', method='GET')
def imagen_obtener_ruta_archivo():
	extension_id = int(request.query.id)
	Extension = Query()
	tmp = extensiones.search(Extension.id == extension_id)
	rpta = None
	if tmp == []:
		rpta = ''
	else:
		rpta = tmp[0] 
	return rpta

@extension_view.route('/extension/listar', method='GET')
def extension_listar():
	return json.dumps(extensiones.all())