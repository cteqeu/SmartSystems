import os
from flask import Flask, jsonify
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api, reqparse
from marshmallow_sqlalchemy import ModelSchema
from datetime import datetime
from collections.abc import Mapping

# made by Vincent Claes
# www.cteq.eu

app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': os.environ['DATABASE_URL'],
    'SQLALCHEMY_TRACK_MODIFICATIONS': True
})
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(80))
    place = db.Column(db.String(120))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)

class TemperatureSchema(ma.ModelSchema):
    class Meta:
        model = Temperature

temperature_schema = TemperatureSchema()
temperatures_schema = TemperatureSchema(many=True)		

# MAIN ROUTE
@app.route('/')
def home():
    return "Hello World!"

# ALL TEMP VALUES	
@app.route('/api/temps/')
def temps():
    all_temps = Temperature.query.all()
    result = temperatures_schema.dump(all_temps)
    return jsonify(result.data)

# TEMP VALUE BY ID	
@app.route('/api/temps/<id>')
def user_detail(id):
    temp = Temperature.query.get(id)
    return temperature_schema.jsonify(temp)	

# NEW VALUE >POST METHOD	
@app.route("/api/temp", methods=["POST"])
def add_temp():
    value = request.json['value']
    place = request.json['place']

    new_temp = Temperature(value=value, place=place)

    db.session.add(new_temp)
    db.session.commit()

    tempe = Temperature.query.get(new_temp.id)

    return temperature_schema.jsonify(tempe)

# UPDATE TEMP VALUE	
@app.route("/api/temp/<id>", methods=["PUT"])
def user_update(id):
    tempe = Temperature.query.get(id)
    value = request.json['value']
    place = request.json['place']

    tempe.value = value
    tempe.place = place

    db.session.commit()
    return temperature_schema.jsonify(tempe)
	
# DELETE TEMP VALUE 
@app.route("/api/temp/<id>", methods=["DELETE"])
def user_delete(id):
    tempe = Temperature.query.get(id)
    db.session.delete(tempe)
    db.session.commit()

    return temperature_schema.jsonify(tempe)	
	
if __name__ == '__main__':
    app.run()
