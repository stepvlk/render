from flask import Blueprint, request
ui_routes = Blueprint('ui_routes', __name__, static_folder='static', template_folder='ui_route/templates')
import graph.render as Visual




@ui_routes.route(f'/api/v2/{config["server"]["stand"]}/render_image',methods=['GET', 'POST'])
def render_image():
    if request.method == "GET":
        resp = Visual.Networks.generate_graph(request.args)
        way = Visual.Networks.generate_png(resp)
    if request.method == "POST":
        resp = Visual.Networks.generate_graph(request.get_json())
        way = Visual.Networks.generate_png(resp)
    return way

@ui_routes.route(f'/api/v2/{config["server"]["stand"]}/render_image_long',methods=['GET', 'POST'])
def render_image_long():
    if request.method == "GET":
        resp = Visual.Networks.generate_graph(request.args)
        way = Visual.Networks.generate_long_png(resp)
    if request.method == "POST":
        resp = Visual.Networks.generate_long_png(request.get_json())
        way = Visual.Networks.generate_png(resp)
    return way