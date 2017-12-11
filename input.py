from flask import Flask, send_from_directory, request, render_template
app = Flask(__name__)

@app.route('/input', methods=['GET','POST'])
def send():
	if request.method == 'POST':
		age = request.form['age']

		return render_template('age.html', age=age)

	return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)