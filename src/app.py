from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos=[ { "label": "My first task", "done": False } ]



@app.route('/todos', methods=['GET'])
def hello_world():
    body = jsonify(todos)
    return body

@app.route('/todos', methods=['POST'])
def add_new_todo():
    body= request.data
    decoded_task=json.loads(body)
    todos.append(decoded_task)
    return jsonify(todos) 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    print("This is the position to delete: ",position)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)



# pipenv run python src/app.py