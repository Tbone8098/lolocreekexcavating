from flask_app import app
from flask_app.controllers import controller_business_info, controller_routes, controller_user, controller_service

if __name__=='__main__':
    app.run(debug=True)