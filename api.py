import csv

from flask import Flask, jsonify

app = Flask(__name__)

pacotes = []


def load_data():
    with open('informacoes_pacotes.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            pacotes.append(row)


@app.route('/pacotes', methods=['GET'])
def get_packages():
    return jsonify(pacotes)


@app.route('/pacotes/nome', methods=['GET'])
def sort_by_name():
    sorted_packages = sorted(pacotes, key=lambda p: p['Nome'])
    return jsonify(sorted_packages)


@app.route('/pacotes/data_publicacao', methods=['GET'])
def sort_by_date_published():
    sorted_packages = sorted(pacotes, key=lambda p: p['Data de publicacao'])
    return jsonify(sorted_packages)


@app.route('/pacotes/versao_python', methods=['GET'])
def sort_by_python_version():
    sorted_packages = sorted(
        pacotes, key=lambda p: p['Versao Python mais recente'])
    return jsonify(sorted_packages)


@app.route('/pacotes/downloads_ultimo_mes', methods=['GET'])
def sort_by_downloads_last_month():
    sorted_packages = sorted(
        pacotes, key=lambda p: p['Downloads no ultimo mes'])
    return jsonify(sorted_packages)


@app.route('/pacotes/nome/<name>', methods=['GET'])
def search_by_name(name):
    results = [p for p in pacotes if p['Nome'] == name]
    return jsonify(results)


@app.route('/pacotes/versao_python/<python_version>', methods=['GET'])
def search_by_python_version(python_version):
    results = [p for p in pacotes if
               p['Versao Python mais recente'] == python_version]
    return jsonify(results)


if __name__ == '__main__':
    load_data()
    app.run(debug=True)
