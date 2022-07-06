from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
conn_info = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432,
    "dbname": "webserver"
}
def get_url(user:str, password:str, host:str, port:int, dbname:str) -> str:
    url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

    return url
url = get_url(**conn_info)
app.config['SQLALCHEMY_DATABASE_URI'] = url
db = SQLAlchemy(app)


class People(db.Model):  
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    dob = db.Column(db.Date)

    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        

@app.route("/", methods=["GET, POST"])
@app.route("/home", methods=["POST"])
def home():
    if request.method == "POST":
        key = request.form.get("key")
        return "hello"+key
    return render_template("home.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)


# @app.route("/create")
# def create():
#     return render_template("create.html")


# @app.route("/read")
# def read():
#     return render_template("read.html")


# @app.route("/update")
# def update():
#     return render_template("update.html")


# @app.route("/delete")
# def delete():
#     return render_template("delete.html")


# if __name__ == "__main__":
#     app.run(debug=True)