import json
from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

f = open('pokeGen7.json', encoding="utf8")
data = json.load(f)

class helloWorld(Resource):
    def get(self):
        return {'data':'Hello World!'}

class pokemon(Resource):
    def get(self):
        return {'data': 'Request pokemon/pokemonIDHere or pokemon/pokemonNameHere'}
    
class callPokemon(Resource):
    def get(self,id):
        if id == "all":
            return data
        return data[(int(id)-1)]

class callNameTest(Resource):
    def get(self,name):
     for n in data:
        if name[0].islower():
            name = name[0].upper() + name[1:]
        else:
            name
            if name == n['name']['english']:
                info = {'id':n['id'],
                        'type':n['type'],
                        'base':n['base']
                }
                return info

api.add_resource(callPokemon,'/pokemon/<id>')
api.add_resource(pokemon,'/pokemon')
api.add_resource(helloWorld,'/hello')
api.add_resource(callNameTest, '/nametest/<name>')

if __name__ == '__main__':
    app.run(debug=True, port=8000)