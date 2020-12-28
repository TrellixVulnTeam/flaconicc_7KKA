from flask import Flask, make_response, request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest
from api import processInputFile, validateData, processData


app = Flask(__name__)
api = Api(app, prefix="/parse")
auth = HTTPBasicAuth()

users = {
      "nathan": generate_password_hash("test")

}
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


class ParseJsonAPI(Resource):
    @auth.login_required
    def post(self):
        errors = {}
        ##Get file fro the body
        ##Get keys from the link
        file = request.files.get('file')
        keys = request.args.getlist('keys')
        if errors:
            raise BadRequest(errors)

        file.save('input_from_request.json')
        data = processInputFile(from_file=True, file='input_from_request.json')
        if validateData(data,keys):
            result = processData(data, keys)
            response = make_response(result)
            return response
        else:
            raise BadRequest({"error": 'File or keys not valid'})

api.add_resource(ParseJsonAPI, '/webapi', endpoint='webapi')

if __name__ == '__main__':
    app.run(debug=True)