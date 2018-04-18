from flask import Flask
from flask import request
from flask import abort
from flask import jsonify

import json

app = Flask(__name__)

data = json.load(open("data.json"))

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/restaurant/<string:res_name>', methods=['GET'])
def get_restaurant(res_name):
    """
    Get restaurant by name
    """
    if res_name not in data:
        return "Restaurant does not exist", 404
    return jsonify(data[res_name]), 200


@app.route('/menuitem/<string:dish_name>', methods=['GET'])
def get_menuitem(dish_name):
    """
    Get menuitem by name. Return all menuitem that may be the same name
    """
    ret_menu = []
    for res in data:
        for menu in data[res]["menu"]:
            for menuitem in data[res]["menu"][menu]:
                if menuitem['dish'] == dish_name:
                    ret_menu.append(menuitem)
    if len(ret_menu)!=0:
        return jsonify(ret_menu), 200
    return "None is found", 404


@app.route('/restaurant/<string:res_name>', methods=['POST'])
def post_restaurant(res_name):
    """
    Add a new restaurant to the database
    """
    if res_name in data:
        return "Restaurant already exists in database", 404
    res_obj = {
        "id": res_name,
            "menu": {
                    "breakfast": [],
                    "lunch": [],
                    "dinner": [],
                    "drinks": []
        }
    }
    data[res_name] = res_obj
    return "Restaurant succesfully added", 201

@app.route('/menuitem/<string:res_name>/<string:menu_name>/<string:menu_item>', methods=['POST'])
def post_menuitem(res_name, menu_name, menu_item):
    """
    Add a new menuitem to the given restaurant and menu
    """
    if res_name not in data:
        return "Restaurant does not exist in database", 404
    menu_item_object = {
        "dish": menu_item,
        "restaurant": res_name
    }
    data[res_name]["menu"][menu_name].append(menu_item_object)
    return "Menuitem for restaurant succesfully added", 201

@app.route('/restaurant/<string:res_name>', methods=['DELETE'])
def delete_restaurant(res_name):
    """
    Delete a restaurant by the name
    """
    if res_name in data:
        del data[res_name]
    else:
        return "Restaurant not in database", 404
    return "Restaurant deleted successfully", 200

@app.route('/menuitem/<string:res_name>/<string:menu_name>/<string:menu_item>', methods=['DELETE'])
def delete_menuitem(res_name, menu_name, menu_item):
    """
    Delete a menuitem by the restaurant, menu and menuitem
    """
    if res_name not in data:
        return "Restaurant does not exist", 404
    dish_exist = 0
    dish_to_delete = None
    for dish in data[res_name]["menu"][menu_name]:
        if dish["dish"] == menu_item:
            dish_exist = 1
            dish_to_delete = dish
            break
    if dish_exist == 0:
        return "The restaurant does not have this menu item", 404
    data[res_name]["menu"][menu_name].remove(dish_to_delete)
    return "Menu item deleted successfully", 200

@app.route('/restaurant/<string:old_res_name>/<string:new_res_name>', methods=['PUT'])
def put_restaurant(old_res_name, new_res_name):
    """
    Change a given restaurant name
    """
    if old_res_name not in data:
        return "Restaurant does not exist", 404
    new_res_object = data[old_res_name]
    del data[old_res_name]
    data[new_res_name] = new_res_object
    data[new_res_name]["id"] = new_res_name
    return jsonify(data[new_res_name])

if __name__ == "__main__":
    app.run()
