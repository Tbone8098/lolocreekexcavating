from flask_app import app
from flask_app.controllers import controller_business_info, controller_routes, controller_user, controller_service, controller_album, controller_image, controller_message

if __name__=='__main__':
    app.run(debug=True)