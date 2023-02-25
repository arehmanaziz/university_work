import numpy as np
import pandas as pd

# Define grading rules based on hours and academic record
def predict_grade(hours, record):
    if hours >= 5 and record in [1, 2]:
        grade = 'A'
    elif hours >= 4 and record in [1, 2]:
        grade = 'B'
    elif hours >= 3 and record in [2, 3]:
        grade = 'C'
    elif hours >= 2 and record in [3, 4]:
        grade = 'D'
    else:
        grade = 'F'
    return grade

# Define a function to preprocess the data
def preprocess_data(data):
    # Convert academic record to numerical values
    record_dict = {'excellent': 1, 'good': 2, 'average': 3, 'poor': 4}
    data['record'] = data['record'].map(record_dict)
    # Scale the hours column
    data['hours'] = data['hours'] / data['hours'].max()
    return data

# Define a function to load the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return preprocess_data(data)

# Define a function to get user input
def get_user_input():
    hours = float(input("Enter the number of hours spent on the subject: "))
    record = input("Enter the student's previous academic record (excellent, good, average, poor): ")
    return hours, record

# Define a function to predict the grade
def predict_grade_advanced(hours, record, data):
    # Preprocess user input
    record_dict = {'excellent': 1, 'good': 2, 'average': 3, 'poor': 4}
    record = record_dict[record]
    hours_scaled = hours / data['hours'].max()
    # Filter the dataset based on academic record
    filtered_data = data[data['record'] == record]
    # Calculate the distance between user input and each data point
    distances = np.abs(filtered_data['hours'] - hours_scaled)
    # Find the index of the closest data point
    closest_index = np.argmin(distances)
    # Get the predicted grade for the closest data point
    predicted_grade = filtered_data.iloc[closest_index]['grade']
    return predicted_grade

# Load the data
data = load_data('grades_dataset.csv')

# Get user input
hours, record = get_user_input()

# Predict the grade
predicted_grade = predict_grade_advanced(hours, record, data)

# Output the predicted grade
print("The predicted grade is:", predicted_grade)
