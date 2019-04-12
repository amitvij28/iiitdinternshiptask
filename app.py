from flask import Flask, render_template,request,redirect
import sys
from utils import readStops
from findroutes import findroutes

app = Flask(__name__)

#Get the name of stops available for th dropdown menu
data=readStops()
stoplist = [x['stop_name'] for x in data ]

#Home Page with all the functionality
@app.route('/',methods = ['GET','POST'])
def index():
    routes={
        'zero':[],
        'one':[]
    }
    sp=""
    ep=""
    flag=True
    if request.method=='POST':
        sp = request.form['StartPoint']
        ep = request.form['EndPoint']
        routes= findroutes(sp,ep)
    if sp=="" and ep=="":
        flag=False
    return render_template('home.html',data=stoplist,routes0=routes['zero'],routes1=routes['one'],sp=sp,ep=ep,flag=flag)

#Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(debug=True)