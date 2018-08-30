#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import environ as env
from sys import argv

import bottle
from bottle import default_app, request, route, response, get

bottle.debug(True)

@route('/')
def hello():
    return "Halló heimur", '''
        <hr>
        <a href="/page/1">Sida 1</a><br>
        <a href="/page/2">Sida 2</a><br>
        <a href="/page/3">Sida 3</a>
    '''

@route('/page/<numer>')
def sida(numer=1):
    return "Síða ", numer, '''
        <hr>
        <a href="/">Index</a>
    '''

bottle.run(host='0.0.0.0', port=argv[1])
