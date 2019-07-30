from flask import Flask

app = Flask(__name__)

from app.main.index import main as main

# ? What is flaskApp.register_blueprint 
app.register_blueprint(main)