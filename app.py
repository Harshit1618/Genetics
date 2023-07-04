from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def hello():
    return "hi"

@app.route("/one")
def one():
    return "one"
@app.route("/zero")
def zero():
    return  "

@app.route("/results/<int:n>")
def hi(n):
    t=""
    if(n==0):
        t+="zero"
    if(n==1):
        t+='one'
    redirect(url_for(t ))
    

if(__name__=="__main__"):
    app.run(debug=True) 