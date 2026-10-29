
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Load the dataset
df = pd.read_csv("student_data.csv")

# 2. Select features and target
X = df[["StudyHours", "Attendance"]]
y = df["Marks"]

# 3. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 4. Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predict marks for the test data
predictions = model.predict(X_test)

# 6. Plot actual vs predicted marks
plt.figure(figsize=(8, 5))

plt.plot(
    range(len(y_test)),
    y_test.to_numpy(),
    marker="o",
    label="Actual Marks"
)

plt.plot(
    range(len(predictions)),
    predictions,
    marker="x",
    label="Predicted Marks"
)

plt.xlabel("Test Student")
plt.ylabel("Marks")
plt.title("Actual vs Predicted Student Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()

print("Opening graph...")
plt.show(block=True)
