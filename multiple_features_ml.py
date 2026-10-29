
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# 1. Load the dataset
df = pd.read_csv("student_data.csv")

print("STUDENT MARKS PREDICTION SYSTEM")
print("--------------------------------")
print("\nDataset:")
print(df)

# 2. Select input features and target
X = df[["StudyHours", "Attendance"]]
y = df["Marks"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 4. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate the model
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

print("\nActual marks:", y_test.tolist())
print("Predicted marks:", predictions.round(2).tolist())
print("Mean Absolute Error:", round(mae, 2))

# 6. Predict marks for a new student
study_hours = float(input("\nEnter study hours: "))
attendance = float(input("Enter attendance percentage: "))

new_student = pd.DataFrame({
    "StudyHours": [study_hours],
    "Attendance": [attendance]
})

predicted_marks = model.predict(new_student)

print("\nPredicted marks:", round(predicted_marks[0], 2))
