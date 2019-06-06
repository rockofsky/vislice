import bottle
import model

vislice = model.Vislice({})

@bottle.get("/")
def uvod():
    return bottle.template("index.tpl")

@bottle.get("/igra/")
def nova_igra()


bottle.run(reloader=True, debug=True)
