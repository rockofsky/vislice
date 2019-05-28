import bottle
import model

vislice = Vislice({})

@bottle.get("/")
def uvod():
    return bottle.template("index.tpl")