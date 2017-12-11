from flask import Flask, make_response, request
app = Flask(__name__)

@app.route("/getcookie")
def getcookie():
	var1 = request.cookies.get('name')
	var2 = request.cookies.get('age')
	return var1 +' '+ var2

if __name__== '__main__':
	app.run(debug=True)
