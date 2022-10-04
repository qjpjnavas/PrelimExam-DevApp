from flask import Flask, jsonify, request 
app = Flask(__name__)

glucose_record = [
    {
        "glucose_id" : "01",
        "date" : "October 4, 2022",
        "glucose" : "90mg"
    },
    {
        "glucose_id" : "02",
        "date" : "October 5, 2022",
        "glucose" : "100mg"
    }
]
@app.route('/insert',methods=['POST','GET'])
def insert(): #insert data
    if request.method == 'POST':
        data = request.get_json()
        if data:
            glucose_record.append(data)
            return 'Data has Added!', 200
    elif request.method == 'GET': #read glucose information
        return jsonify(glucose_record)

@app.route('/edit/<int:index>',methods=['PUT','GET','DELETE'])
def edit(index):
    if request.method == 'PUT': #update specific glucose record
        up_record = request.get_json()
        glucose_record[index] = up_record
        return 'Data has been Updated!', 200
    elif request.method == 'GET': #view specific glucose data
        return jsonify(glucose_record[index])
    elif request.method == 'DELETE': #delete specficic glucose data
        glucose_record.pop(index)
        return 'Data has been Deleted!', 200

if __name__ == '__main__':
    app.run()