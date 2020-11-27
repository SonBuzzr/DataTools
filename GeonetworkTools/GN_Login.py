# Geonetwork login and logout

import requests
import gnconfig as cfg

"""
gnconfig contains user credential and Host url

RDSLogin = {'username': 'username',
            'password': 'password'}

HOST = {'LOCAL': 'URL'}

"""

host = cfg.HOST['Bhutan']

xml_header = {'Content-type': 'application/xml'}
gn_namespace = 'http://www.isotc211.org/2005/gmd/'

gn_loginURL = host + "/j_spring_security_check"
gn_logoutURL = host + "/j_spring_security_logout"

gn_getURL = host + "/srv/eng/xml.metadata.get"
gn_search = host + "/srv/eng/xml.search"
gn_update = host + "/srv/eng/metadata.update"


gn_session = requests.Session()


def gn_login():
    gn_conn = gn_session.post(gn_loginURL, data=cfg.RDSLogin)
    print("Login..", gn_conn)


def gn_logout():
    print("Logout..")
    gn_conn = gn_session.post(gn_logoutURL)


