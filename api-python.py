from flask import Flask, render_template, jsonify
import os
import random
import linecache

# Files

FILE_NAME="random_numbers.txt"

def generate_random_numbers_file():
    random_file = open(FILE_NAME, "w" )
    nums = 4096

    for i in range(nums):
        line = str(random.uniform(-4096, 4096))  + "\n"
        random_file.write(line)
    random_file.close()

def get_value_of_random_numbers_file(row):
    if not os.path.exists(FILE_NAME):
        raise ValueError('File not found')
    return linecache.getline(FILE_NAME, int(row)).strip()
    
# Bussines Logic

def operate(operation, value1, value2):
    if operation == 'suma':
        return value1 + value2
    elif operation == 'resta':
        return value1 - value2
    elif operation == 'multiplicacion':
        return value1 * value2
    elif operation == 'division':
        return value1 / value2
    else:
        raise ValueError('Valid operations \'suma\', \'resta\', \'multiplicacion\', \'division\'')

# Server

def start_server():
    app = Flask(__name__)
    load_server_routes(app)
    app.run(debug=True, host='localhost', port=8080)

def load_server_routes(server_app):
    @server_app.route('/operate/<operation>/<row1>/<row2>')

    def operate_service(operation, row1, row2):
        try:
            value1 = get_value_of_random_numbers_file(row1)
            value2 = get_value_of_random_numbers_file(row2)
            result = operate(operation, value1, value2)
        except Exception as e:
          return "Error: " + str(e)

        dic_response = {
          "linea1": row1,
          "linea2": row2,
          "valorLinea1": value1, 
          "valorLinea2": value2,
          "result": result, 
        }
        return jsonify(dic_response)


# Main

def main():
    generate_random_numbers_file()
    start_server()

main()