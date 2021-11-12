from typing import Any
from flask import Flask, jsonify, request

import json


app = Flask(__name__)

with open("data.json") as file:
    data = json.load(file)


@app.route("/")
def get_all_users():
    return jsonify(list[data])


@app.route("/", methods=["POST"])
def create_new_user():
    new_user: dict[str, Any] = request.json

    with open("data.json") as file:
        data = json.load(file)

    data[new_user["login"]] = {"password": new_user["password"]}

    with open("data.json", "w") as file:
        json.dump(data, file)

    return jsonify({"info": "Success"})


if __name__ == "__main__":
    app.run(debug=True)
