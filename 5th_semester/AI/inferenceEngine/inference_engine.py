import pandas as pd

# Function to load the data
def load_data(filename):
    data = pd.read_csv(filename)
    return data


# Function to get user input
def get_user_input():
    hours = float(input("Enter the number of hours spent on the subject: "))
    record = input("Enter the student's previous academic record (excellent, good, average, poor): ")
    return hours, record


if __name__ == "__main__":
    # load the data
    data = load_data("grades_dataset.csv")
    print(data)

    # get user input
    hours, record = get_user_input()

