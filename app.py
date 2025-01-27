from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

#load trained model
model_path = 'model.pkl'
with open(model_path,'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # extract data from form
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    #make predictation
    output = model.predict(final_features)

    
    return render_template('index.html',prediction_text = 'Prediction: {} crore'.format(round(output[0],2)))

if __name__ == '__main__':
    app.run(debug=True)
