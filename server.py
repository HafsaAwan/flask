from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    signed_in = False # we are hardcoding this just to demonstrate how we can do conditionals in our template files, in future we won't be hardcoding this.
    return render_template('index.html', signed_in=signed_in)

@app.route("/another")
def show():
    return '<h1>Yo</h1>'

 

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run()