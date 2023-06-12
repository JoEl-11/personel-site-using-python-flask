from flask import Flask,render_template
app=Flask(__name__)


@app.route('/')
def hello():
    return render_template('/index.html')

@app.route('/institutions')
def inst():
    return render_template('institutions.html')

@app.route('/favorite teams')
def fav():
    return render_template('/favorite teams.html')

@app.route('/contactme')
def con():
    return render_template('/contact me.html')

if (__name__ == "__main__"):
    app.run(debug=True,port=8000)