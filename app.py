from flask import Flask, render_template,request,redirect

import sys

app = Flask(__name__)


@app.route('/')
def index():
    data=['Delhi','Mumbai','Chennai']
    return render_template('home.html',data=data)

@app.route('/gettingdata',methods = ['GET','POST'])
def gettingdata():
    if request.method=='POST':
        sp = request.form['StartPoint']
        ep = request.form['EndPoint']
        print(sp+" "+ ep ,file=sys.stdout)

    return redirect('/')    


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')





if __name__ == "__main__":
    app.run(debug=True)