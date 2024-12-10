from flask_pymongo import PyMongo
from flask_cors import CORS

# MongoDB-Instanz
mongo = PyMongo()

def init_extensions(app):
    """
    Initialisiere die Erweiterungen der Flask-Anwendung.
    """
    # Initialisiere MongoDB
    mongo.init_app(app)

    # Aktiviere CORS (Cross-Origin Resource Sharing) für die App
    CORS(app)
