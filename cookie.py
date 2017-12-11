from flask import Flask, make_response
app = Flask(__name__)
@app.route("/setcookie")
def hello():
	resp = make_response('Setting cookie!')
	resp.set_cookie('name','Aniket')
	resp.set_cookie('age','19')
	return resp

if __name__== '__main__':
	app.run(debug=True)
