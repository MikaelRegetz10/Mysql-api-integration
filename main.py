from flask import Flask, request, jsonify
import models.queries as queries
import flask

app = Flask(__name__)
flask.json.provider.DefaultJSONProvider.sort_keys = False


@app.route("/consumables", methods=["GET"])
def get_consumables():
    if request.method == 'GET':
        consumables = queries.select_all_infos()
        if consumables['status']:
            return jsonify(consumables['data']), 200

        return 'Internal Server Error', 500

    else:
        return 'Method Not Allowed', 405

@app.route("/consumables/add", methods=["POST"])
def add_consumables():
    if request.method == 'POST':

        name = request.form['name']
        buy = request.form['buy']
        sell = request.form['sell']
        type = request.form['type']
        link = request.form['link']

        allowed_types = ['Poções', 'Mágicos', 'Alquímicos']
        if type not in allowed_types:
            return 'Invalid type. Choose between Poções, Mágicos or Alquímicos.'

        new_consumables = queries.add_new_consumable(name, buy, sell, type, link)
        if not new_consumables['status']:
            return 'Internal Server Error', 500

        return jsonify(new_consumables['data']), 201

    else:
        return 'Method Not Allowed', 405

@app.route("/consumables/<int:id>", methods=["GET"])
def get_consumable_by_id(id):
    if request.method == 'GET':

        consumables = queries.select_all_infos()
        if not consumables['status']:
            return 'Internal Server Error', 500

        for consumable in consumables["data"]:
            if consumable['id'] == id:
                return jsonify(consumable)

        return 'Not Found', 404

    else:
        return 'Method Not Allowed', 405

@app.route("/consumables/delete/<int:id>", methods=["DELETE"])
def delete_consumable_by_id(id):
    if request.method == 'DELETE':
        consumable = queries.delete_consumable(id)
        if not consumable['status']:
            return 'Internal Server Error', 500

        if consumable['not_fould']:
            return 'Not Found', 404

        return 'No Content', 204

    else:
        return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(debug=True)