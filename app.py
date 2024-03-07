from flask import Flask, render_template, jsonify
from flask_cors import CORS
from data_pasien import data_pasien

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/data-pasien', methods=['GET'])
def get_data_pasien():
    return jsonify(data_pasien)


@app.route('/', methods=['GET'])
def index_page():
    return render_template('index.html', data_pasien=data_pasien)

@app.route('/detail/<string:pasien_id>', methods=['GET'])
def detail_pasien_page(pasien_id):
    pasien = next((pasien for pasien in data_pasien if pasien['id'] == pasien_id), None)
    if pasien:
        return render_template('detail.html', pasien=pasien)
    else:
        return 'Pasien not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
