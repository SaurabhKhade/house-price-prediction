from flask import Flask, render_template, request, json
from flask_cors import CORS
import pickle

app = Flask(__name__, static_url_path='', template_folder='static')
CORS(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = json.loads(request.data)
        with open('./model_rent_p', 'rb') as f:
            lr = pickle.load(f)
            pr = lr.predict([[data['latitude'], data['longitude'], data['gym'], data['lift'], data['pool'], data['negotiable'],
                            data['property'], data['age'], data['bathrooms'], data['cupboards'], data['floor'], data['n_floors'], data['balcony']]])
            return str(pr[0])
    except Exception as e:
        print(e)
        return "Error Occured"


if __name__ == '__main__':
    app.run()
