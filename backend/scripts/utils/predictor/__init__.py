import pickle
import numpy as np


# Function to predict crop for new data
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    # Load the trained model and scaler
    with open('backend/scripts/utils/predictor/svm_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('backend/scripts/utils/predictor/scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    # Create input array
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    return prediction[0]
