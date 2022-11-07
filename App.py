from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        "Contact" : "9987644456",
        "Name" : "Raju" ,
        "done" : False,
        "id" : 1
    },
    {
        "Contact" : "1234567890",
        "Name" : "Rahul" ,
        "done" : False,
        "id" : 2
    }
]


@app.route("/add-data" , methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
        
    contact = {
        "id" : data[-1]['id'] + 1,
        'Name' : request.json['Name'],
        "Contact" : request.json['Contact'],
        "done" : False
    }
    data.append(contact)
    return jsonify({
        "status" : "Success" ,
        "message" : "Contact Added Successfully!"
    })


    