from flask import Flask, send_from_directory, request, render_template
app = Flask(__name__)



@app.route('/robots.txt')
def static_from_root():
 return send_from_directory(app.static_folder, request.path[1:])



if __name__ == '__main__':
   app.run(debug = True)