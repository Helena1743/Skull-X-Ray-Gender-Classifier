import os
import tensorflow as tf
from flask import Flask
from routes import main
from auth import auth

# Disable GPU (optional, to suppress CUDA warnings on Render)
tf.config.set_visible_devices([], 'GPU')

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a secure key in production

# Config
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load Routes
app.register_blueprint(auth)
app.register_blueprint(main)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Use Render's PORT, default to 10000
    app.run(host='0.0.0.0', port=port, debug=False)  # debug=False for production
