from flask import Flask, render_template
from flask.globals import request 
import requests
import json
from pokeclasse import Pokemon

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/search_name", methods=["GET", "POST"])
def buscar_nome():
    pokename = Pokemon(request.form["nome"].lower(),"","","")
    try:
        res = json.loads(requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokename.nome}').text)
        sprite = res["sprites"]
        sprite = sprite["front_default"]
        pokename.foto = sprite


        poderes = res['moves']
        for i in poderes:
            pokename.moves = i['move']['name']
        print("\nMove:"+str(pokename.moves))


        habilidades = res['abilities']
        for x in habilidades:
            pokename.habilidade = x['ability']['name']
        print('\nAbilities:'+str(pokename.habilidade))


    except:
        return render_template('telaerror.html')
    return render_template("index.html",
    nome = res["name"], 
    moves = pokename.moves,
    foto = pokename.foto,
    habilidade = pokename.habilidade
    )


if __name__ == '__main__':
    app.run(debug=True)

