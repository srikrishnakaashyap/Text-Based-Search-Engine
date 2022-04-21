from flask import Flask
from flask_cors import CORS

from werkzeug.middleware.proxy_fix import ProxyFix
from initializers.register_all_blueprints import RegisterBlueprints
# from initializers.register_all_blueprints import RegisterBlueprints

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_port=1)

with app.app_context():
    # from services.setup_config import SetupConfig
    # SetupConfig(app)
    # db.init_app(app)

    # RegisterBlueprints(app, db)
    CORS(app)
    RegisterBlueprints(app)
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.run(host = "0.0.0.0", port=5002,)

    print("...Default Web Mode Completed")
