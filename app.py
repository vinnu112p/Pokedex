from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    pokemon = None
    if request.method == "POST":
        pokemon_name = request.form.get("pokemon_name").lower()
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        if response.status_code == 200:
            data = response.json()
            abilities = [ability['ability']['name'].capitalize() for ability in data['abilities']]
            pokemon = {
                "name": data["name"].capitalize(),
                "image_url": data["sprites"]["front_default"],
                "height": data["height"],
                "weight": data["weight"],
                "abilities": abilities,
                "types": [t["type"]["name"].capitalize() for t in data["types"]]
            }
    return render_template("index.html", pokemon=pokemon)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)