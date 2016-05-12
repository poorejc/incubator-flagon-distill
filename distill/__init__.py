'''
Distill: This package contains a flask app RESTful api for distill

Copyright 2016, The Charles Stark Draper Laboratory
Licensed under Apache Software License.
'''

from __future__ import absolute_import
import sys
from flask import Flask
from elasticsearch_dsl.connections import connections

if sys.version_info[:2] < (2, 7):
    m = "Python 2.7 or later is required for Distill (%d.%d detected)."
    raise ImportError (m % sys.version_info[:2])
del sys

# Initialize Flask instance
my_app = Flask (__name__)

# Load Configurations
my_app.config.from_pyfile('config.cfg')

# Unpack Elasticsearch configuration and create elasticsearch connection
host = my_app.config ['ES_HOST']
port = my_app.config ['ES_PORT']
http_auth = my_app.config ['HTTP_AUTH']
use_ssl = my_app.config ['USE_SSL']
verify_certs = my_app.config ['VERIFY_CERTS']
ca_certs = my_app.config ['CA_CERTS']
client_cert = my_app.config ['CLIENT_CERT']
client_key = my_app.config ['CLIENT_KEY']

# Initialize Elasticsearch instance 

es = connections.create_connection (hosts = [host], \
								   	port = port, \
								   	http_auth = http_auth, \
								   	use_ssl = use_ssl, \
								   	verify_certs = verify_certs,
								   	ca_certs = ca_certs, \
								   	client_cert = client_cert, \
								   	client_key = client_key)