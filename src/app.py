from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  # Obtiene el cuerpo de la solicitud como un diccionario
    todos.append(request_body)    # Agrega el nuevo todo a la lista
    return jsonify(todos)          # Retorna la lista actualizada

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
     if 0 <= position < len(todos):  # Verifica que la posición sea válida
        todos.pop(position)  # Elimina el todo en la posición dada
        return jsonify(todos)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)