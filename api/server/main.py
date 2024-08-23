# Imports
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Setup
Client = MongoClient('mongodb+srv://ToughLuck:GH3ZdTrswe1lg2KD@bitnsfw.ytfzx.mongodb.net/?retryWrites=true&w=majority&appName=BitNSFW')
DataBase = Client.get_database('BitNSFWDiscordAccounts')
Accounts = DataBase.get_collection('Accounts')

app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')
CORS(app)

# Main Routes

@app.route('/', methods=['GET'])
def main():
    return render_template('main.html')

@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

@app.route('/register-account', methods=['POST', 'GET'])
def register_account():
    if request.method == 'POST':
        # Validate request data
        username = request.form.get('Username')
        if not username:
            return jsonify('Failed! Username is required.'), 400

        # Register account
        registered_account = {
            "Username": username,
            "UserIP": request.remote_addr
        }

        try:
            Accounts.insert_one(registered_account)
            return jsonify('Success!'), 201
        except Exception as e:
            print(f'Error: {e}')
            return jsonify('Failed to register account!'), 500
    else:
        return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
