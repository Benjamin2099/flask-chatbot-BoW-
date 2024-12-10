import os
import random
import json
from flask import request, jsonify
from . import chatbot_bp
from .model import NeuralNet
from .utils import tokenize_sentence, bag_of_words

# Modell und Intents laden
MODEL_PATH = 'model.pth'
INTENTS_PATH = 'intents.json'

with open(INTENTS_PATH, 'r', encoding='utf-8') as file:
    intents = json.load(file)

# Dummy-Modell (nur zu Demonstrationszwecken)
model = NeuralNet()

@chatbot_bp.route('/message', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'Message is required'}), 400
    
    # NLP-Verarbeitung und Antwort generieren
    processed_message = tokenize_sentence(user_message)
    bot_response = get_response(processed_message)
    
    return jsonify({'response': bot_response})

def get_response(message):
    for intent in intents['intents']:
        if any(phrase in message for phrase in intent['patterns']):
            return random.choice(intent['responses'])
    return "Entschuldigung, ich habe das nicht verstanden."
