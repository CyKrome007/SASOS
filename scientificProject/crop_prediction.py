import numpy as np
import pandas as pd
import pickle


# Function to predict crop for new data
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    # Load the trained model and scaler
    with open('svm_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    # Ensure the input data is in the same format as the training data
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

    # Scale the input data
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)

    return prediction[0]


# Function to take user input
def get_user_input():
    print("Please enter the following information to predict the crop:")

    # Taking input from the user for each feature
    N = float(input("Enter Nitrogen (N) value: "))
    P = float(input("Enter Phosphorus (P) value: "))
    K = float(input("Enter Potassium (K) value: "))
    temperature = float(input("Enter temperature in Celsius: "))
    humidity = float(input("Enter humidity percentage: "))
    ph = float(input("Enter pH value of the soil: "))
    rainfall = float(input("Enter rainfall in mm: "))

    return N, P, K, temperature, humidity, ph, rainfall


# Main function to get user input and predict the crop
def main():
    N, P, K, temperature, humidity, ph, rainfall = get_user_input()

    # Predict the crop based on user input
    predicted_crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)

    # Print the recommended crop
    print(f"Recommended crop for the given conditions: {predicted_crop}")


# Run the main function to get input and make prediction
if __name__ == "__main__":
    main()
