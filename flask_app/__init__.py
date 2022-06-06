from flask import Flask
import os
import cloudinary

app = Flask(__name__)
app.secret_key = 'Whos your daddy? Goons your daddy!'

DATABASE_SCHEMA = 'lolocreekexcavating_db'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# cloudinary.config( 
#   cloud_name = os.environ.get('CLOUD_NAME'), 
#   api_key = os.environ.get('CLOUD_API_KEY'), 
#   api_secret = os.environ.get('CLOUD_API_SECRET') 
# )
