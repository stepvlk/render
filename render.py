#modules
from flask import Flask
from flask_cors import CORS
import logging
from prometheus_flask_exporter import PrometheusMetrics

from route.routes_ui import ui_routes
from config.config import config

#app create
app = Flask(__name__, static_folder='react_ui/build/static', template_folder='react_ui/build')
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
metrics = PrometheusMetrics(app)
metrics.info('ui_netmon_render', 'production_version', version='1.4.3')
app.register_blueprint(ui_routes)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

#main start app
if __name__ == "__main__":
    app.run(host=config['server']['host'], port=config['server']['port'])
