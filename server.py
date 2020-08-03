from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>")
def index(name):
    name = name.upper()
    return render_template('index.html', name=name)

@app.route("/another")
def show():
    return '<h1>Yo</h1>'

 

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()