from flask_restful import Api
from flask import Flask
import new_file

app = Flask(__name__)

api = Api(app)

@app.route("/")
def home():
    return "<h1 style='color:blue'> This is the trying heroku file </h1>"



@app.route("/do_math")
def maths():
    result = new_file.do_math()
    print(result)
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)