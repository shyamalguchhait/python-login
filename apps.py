from flask import Flask, render_template,request
import csv
x=[]
y=[]
with open ("value.csv","r") as csvfile:
    plots =csv.reader(csvfile,delimiter=",")
    for row in plots:
        x.append(row[0])
        y.append(row[1])
l=len(x)
app=Flask(__name__)

@app.route("/")
def Index():
    return render_template ("index.html")
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="GET":
        return "The method is post enter your name and password"
    else:
         
        name=request.form.get("name")
        password=request.form.get("password")
        for i in range(l):
            if name==x[i] and password==y[i]:

                return render_template("login.html",name=name)
        
        return "name or password incorrct"