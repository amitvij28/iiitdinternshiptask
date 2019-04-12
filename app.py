from flask import Flask, render_template,request,redirect
import sys
from utils import readStops
from findroutes import findroutes

app = Flask(__name__)

data=readStops()
stoplist = [x['stop_name'] for x in data ]

@app.route('/',methods = ['GET','POST'])
def index():
    routes={
        'zero':[],
        'one':[]
    }
    if request.method=='POST':
        sp = request.form['StartPoint']
        ep = request.form['EndPoint']
        routes= findroutes(sp,ep)
    
    return render_template('home.html',data=stoplist,routes0=routes['zero'],routes1=routes['one'],sp=sp,ep=ep)

# @app.route('/gettingdata')
# def gettingdata():
#     routes=[]
#     if request.method=='POST':
#         sp = request.form['StartPoint']
#         ep = request.form['EndPoint']
#         routes= findroutes(sp,ep)
        
#         #print(f'Starting Point = {sp}\nEnding Point = {ep}',file=sys.stdout)

#     return render_template('home.html',data=stoplist,routes0=routes['zero'],routes1=routes['one'])   





@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')





if __name__ == "__main__":
    
    app.run(debug=True)