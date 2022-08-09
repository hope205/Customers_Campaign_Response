from flask import Flask, request, jsonify
import  model_files.ml_model as ml
import pickle


app = Flask('app')


@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'  


@app.route('/predict',methods=['POST']) 
def prediction():
    customer_data = request.get_json()
   
    
   
    with open('./model_files/campaign_model.sav', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
   
    predictions = ml.predict_res(customer_data, model)
    result = {
        'Customer_prediction': predictions.tolist()
    }
    
    return jsonify(result)
    
    

if __name__ == "__main__":
    app.run()
