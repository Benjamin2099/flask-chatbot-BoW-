from flask import Flask
from .extensions import init_extensions

def create_app():
    app = Flask(__name__)

    # Konfiguriere die MongoDB-URI (ersetze mit deiner URI in einer echten App)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/chatbot"

    # Initialisiere Erweiterungen
    init_extensions(app)

    # Blueprint registrieren
    from .chatbot import chatbot_bp
    app.register_blueprint(chatbot_bp, url_prefix='/chatbot')

    return app
