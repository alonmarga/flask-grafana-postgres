from flask import Blueprint, request, jsonify, render_template
import psycopg2
from dotenv import load_dotenv
import os
from bcrypt import checkpw, hashpw, gensalt
import jwt

load_dotenv()


main_routes = Blueprint('app',__name__)
auth_routes = Blueprint('auth', __name__)

@main_routes.route('/dash')
def index():
    return render_template('dashboard.html')


# @auth_routes.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')

#         # Fetch credentials from the database
#         connection = psycopg2.connect(os.getenv('DATABASE_URL'))
#         cursor = connection.cursor()

#         cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
#         user = cursor.fetchone()

#         cursor.close()
#         connection.close()

#         if user and checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
#             # Generate and return JWT token
#             payload = {'username': username}
#             secret_key = os.getenv('SECRET_KEY')
#             token = jwt.encode(payload, secret_key, algorithm='HS256')
#             return jsonify({'token': token}), 200
#         else:
#             return jsonify({'message': 'Invalid credentials'}), 401

#     # Render the login form
#     return render_template('login_form.html')
