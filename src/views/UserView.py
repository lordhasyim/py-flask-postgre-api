#/src/views/UserViews

from flask import request, json, Response, Blueprint
from ..models.UserModel import UserModel, UserSchema
#from ..shared.Authentication import Auth

user_api = Blueprint('users', __name__)
user_schema = UserSchema()

@user_api.route('/', methods=['POST'])
def create():
    """
    Create User Function
    """
    req_data = request.get_json()
    data, error = user_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    #check if user already exist in db
    
    user_in_db = UserModel.get_user_by_email(data.get('email'))
    if user_in_db:
        message = {'error' : 'User already exist, use another email'}
        return custom_response(message, 400)
    
    user = UserModel(data)
    user.save()

    ser_data = user_schema.dump(user).data

    return custom_response({'jwt_token' : 'not implemented yet'}, 201)

@user_api.route('/', methods=['GET'])
def get_all():
    users = UserModel.get_all_users()
    ser_users = user_schema.dump(users, many=True).data
    return custom_response(ser_users, 200)

def custom_response(res,status_code):
    """
    Custom Response Function
    """

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )