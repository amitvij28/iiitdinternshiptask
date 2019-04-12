from flask import Flask, render_template,request,redirect
import sys
from utils import readStops
from findroutes import workondata

app = Flask(__name__)

data=readStops()
stoplist = [x['stop_name'] for x in data ]

@app.route('/')
def index():
    
    return render_template('home.html',data=stoplist)

@app.route('/gettingdata',methods = ['GET','POST'])
def gettingdata():
    routes=[]
    if request.method=='POST':
        sp = request.form['StartPoint']
        ep = request.form['EndPoint']
        routes= workondata(sp,ep)

        #print(f'Starting Point = {sp}\nEnding Point = {ep}',file=sys.stdout)

    return render_template('home.html',data=stoplist,routes=routes)   


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')





if __name__ == "__main__":
    
    app.run(debug=True)