from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# @app.after_request
# def add_security_headers(response):
#     # Configurar a política COOP (Cross-Origin-Opener-Policy)
#     response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    
#     # Configurar a política COEP (Cross-Origin-Embedder-Policy)
#     response.headers['SECURE_CROSS_ORIGIN_OPENER_POLICY'] = 'unsafe-none'
    
#     return response

from views import *

if __name__ == "__main__":
   app.run(debug=True)