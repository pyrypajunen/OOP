### IMPORTS ###'
import justpy as jp
from api import Api
from documentation import Documentation


jp.Route("/api", Api.serve)
jp.Route("/", Documentation.serve)
jp.justpy()
        