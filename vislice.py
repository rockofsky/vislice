import bottle
from model import Igra, Vislice

vislice = Vislice({})

@bottle.get("/")
def uvod():
    return bottle.template("index.tpl")


bottle.run(reloader=True, debug=True)
