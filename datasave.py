import pymongo
from flask import Flask, request, render_template


app = Flask(__name__)
# db_connect = pymongo.MongoClient("mongodb://localhost:27017")  # connect to the database
db_connect = pymongo.MongoClient(
    "mongodb+srv://pravinsinh27:shivay27@cluster0.lksygvr.mongodb.net/?retryWrites=true&w=majority",connect=True)  # connect to the database
db = db_connect["test_db2"]  # get database
collection = db["col2"]


@app.route("/test",methods=["GET","POST"])
def add_data():
    if request.method=="POST":
        username=request.form["username"]
        surname=request.form["surname"]
        city=request.form["city"]
        mo_no=request.form["mo_no"]
        dict2={"username":username,"surname":surname,"city":city,"mo_no":mo_no}
        db.col2.insert_one(dict2)

    return render_template("test2.html")


if __name__=="__main__":
    app.run(debug=True,port=4682)

