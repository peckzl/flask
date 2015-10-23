# ---- Flask Hello World ---- #

#import Flask class from the flask package
from flask import Flask

#create the app object
app = Flask(__name__)

#user decorators to link the function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

#start the development server using the run() method
if __name__ == "__main__":
	app.run()