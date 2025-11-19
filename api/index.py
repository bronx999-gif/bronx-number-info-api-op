from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '{
  "success": true,
  "result": [
    {
      "id": 1205627021,
      "mobile": "7676184626",
      "name": "Shivalingappa ",
      "father_name": "Durugappa ",
      "address": "S/O: Durugappa!257!!harijana colony!nadanga  !Nadanga!Bellary!Karnataka!583114",
      "alt_mobile": "",
      "circle": "AIRTEL KARNATKA",
      "id_number": "",
      "email": ""
    },
    {
      "id": 1205627022,
      "mobile": "7676184626",
      "name": "Shivalingappa",
      "father_name": "Durugappa",
      "address": "S/O  Durugappa!!257 harijana colony!nadanga!Nadanga Bellary!Karnataka!583114",
      "alt_mobile": "919901542381",
      "circle": "KARNATAKA JIO ",
      "id_number": "",
      "email": ""
    }
  ],
  "credit": "@BRONX_ULTRA"
}'

@app.route('/about')
def about():
    return 'About'
