import json
from flask import Blueprint, request, jsonify, render_template
from mes_web.utils.socket_common import client_send

blue_print = Blueprint("lot", __name__)


# 工单管理页面
@blue_print.route("/lot", methods=["GET", "POST"])
def lot():
    if request.method == "GET":
        request_flag = {"current_lot": ""}
        current_lot_info = client_send(json.dumps(request_flag))
        kwargs = {
            "current_lot": current_lot_info.get("current_lot", ""),
            "recipes": current_lot_info.get("recipes", []),
            "current_recipe": current_lot_info.get("current_recipe", ""),
            "plc_state": get_plc_state(current_lot_info.get("state"), current_lot_info.get("plc_connect_state"))
        }
        return render_template("cyg_lot.html", **kwargs)


# 点击新建工单按钮
@blue_print.route("/submit_new_lot", methods=["POST"])
def submit_new_lot():
    form_data = request.get_json()
    lot_id = form_data.get("lot_id")
    recipe = form_data.get("recipe")
    request_flag = {"new_lot": {"lot_id": lot_id, "recipe": recipe}}
    result = client_send(json.dumps(request_flag))
    return jsonify(result)


def get_plc_state(mes_state, plc_state):
    if plc_state:
        return "Online"
    else:
        if mes_state == 1:
            return "Offline"
        elif mes_state == -1:
            return "MES server is not running!"

