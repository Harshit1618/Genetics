from flask import Flask,redirect,url_for,render_template,request
import pandas as pd

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method=='POST':
        s=str(request.form['dna'])
        s=s.upper()
        s=s.strip()
        if(s.endswith('.')):
            s=s[:-1]
        if(len(s)==9  and ''.join(sorted(list(set(list(s))))) in 'ACGT'):
            return render_template("results.html",dna_str=s,subpopulation="tropicana",height=100)
        else:
            return render_template("invalid.html")

if(__name__=="__main__"):
    app.run(debug=True) 
    
    
    
