import pickle
import numpy as np


# Function to predict crop for new data
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    # Load the trained model and scaler
    with open('svm_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    # Create input array
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Scale the input
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    return prediction[0]


# Example of using the function with new data
predicted_crop = predict_crop(90, 42, 43, 20.87, 82.00, 6.50, 202.93)
print(f"Recommended crop for the given conditions: {predicted_crop}")
