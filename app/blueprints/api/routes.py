from flask import jsonify, request, redirect
from . import bp as app
from app.blueprints.main.models import Car
from app import db



@app.route("/create_car", methods=["POST"])
def create_car():
    user = 1

    make = request.form['make']
    model = request.form['model']
    year = request.form['year']
    color = request.form['color']
    price = request.form['price']

    new_car = Car(user_id=user, make=make, model=model, year=year, color= color, price=price)

    db.session.add(new_car)
    db.session.commit()

    return redirect("http://127.0.0.1:5000/")