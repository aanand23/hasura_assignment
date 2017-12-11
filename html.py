from flask import Flask

app = Flask(__name__)
@app.route("/html")
def homepage():
		return "<h2>Homepage</h2>"

if __name__ == '__main__':
	app.run(debug=True)