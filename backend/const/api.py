class AuthEndpoints:
    PREFIX = '/auth'
    TAGS = ['AUTHENTICATION']
    LOGIN = '/login'
    REGISTER = '/register'

class UserEndpoints:
    PREFIX = '/user'
    TAGS = ['USER']
    GET_USER = '/<int:user_id>'
    GET_ALL_USERS = '/'
    UPDATE_USER = '/<int:user_id>'
    DELETE_USER = '/<int:user_id>'
    LOGOUT = '/logout'
    PROFILE = '/profile'

class PredictionEndpoints:
    PREFIX = '/predict'
    TAGS = ['PREDICTION']
    PREDICT = '/'