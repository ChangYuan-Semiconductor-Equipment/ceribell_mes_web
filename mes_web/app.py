from flask import Flask
from blueprints.index import blue_print as index_blue_print
from blueprints.lot import blue_print as lot_blue_print


app = Flask(__name__)
app.register_blueprint(index_blue_print)
app.register_blueprint(lot_blue_print)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2024, debug=True)
