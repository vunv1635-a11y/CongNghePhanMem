# API xác thực email Google
from flask import Blueprint, request, jsonify
from src.api.email_google import email_google_bp
email_google_bp = Blueprint('email_google', __name__)

@email_google_bp.route('/verify_email', methods=['POST'])
def verify_email():
    data = request.get_json()
    email = data.get('email')
    # Logic xác thực email Google ở đây
    return jsonify({"message": "Email verified successfully"}), 200

def register_email_google_routes(app):
    app.register_blueprint(email_google_bp, url_prefix='/api/email_google')