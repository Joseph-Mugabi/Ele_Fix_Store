#!/usr/bin/env python3

from flask import request, jsonify, abort
import requests
from os import getenv
from api.v1.blueprints import app_views

@app_views.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Get the JSON data from the request
    message = data['message']  # Extract the user's message

    # Call the ChatGPT API
    response = call_chatgpt_api(message)

    return jsonify(response)

def call_chatgpt_api(message):
    api_key = getenv("API_KEY")
    endpoint = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
         "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": message}],
     "temperature": 0.7
    }

    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()

    return response_data["choices"][0]["message"]["content"]
