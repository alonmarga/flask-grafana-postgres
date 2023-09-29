from flask import Flask, render_template
from routes.routes import main_routes,auth_routes
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes, url_prefix='/auth')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
