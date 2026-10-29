
# Student Marks Prediction System 🎓

## 📌 About the Project
This is a beginner Machine Learning project that predicts student marks using study hours and attendance percentage.

The project uses Linear Regression to learn patterns from a sample dataset and predict marks for new student inputs.

## 🎯 Objectives
- Learn the basics of Machine Learning.
- Work with a CSV dataset using Pandas.
- Train and evaluate a Linear Regression model.
- Predict marks using multiple input features.
- Visualize actual and predicted marks.

## 🛠️ Technologies Used
- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

## 📂 Project Structure
```text
Student-Marks-Prediction/
├── student_data.csv
├── multiple_features_ml.py
├── prediction_graph.py
└── README.md
```

## 📊 Dataset
The sample dataset contains three columns:

| Column | Description |
|---|---|
| StudyHours | Hours spent studying |
| Attendance | Attendance percentage |
| Marks | Student marks |

**Note:** This project uses a small sample dataset for learning purposes. It is not intended to make reliable predictions about real students.

## ⚙️ Installation

Install Python, then open a terminal in the project folder.

Install the required libraries:

```bash
python -m pip install pandas numpy scikit-learn matplotlib
```

## ▶️ How to Run

### 1. Predict Student Marks

```bash
python multiple_features_ml.py
```

Enter the student's study hours and attendance percentage when prompted.

### 2. View the Prediction Graph

```bash
python prediction_graph.py
```

A graph will display actual marks compared with predicted marks.

## 📈 Model Evaluation
The model is evaluated using Mean Absolute Error (MAE).

A lower MAE generally indicates that predictions are closer to actual values. Because this project uses a small sample dataset, the evaluation result should not be treated as proof of real-world accuracy.

## 📚 What I Learned
- Python programming fundamentals
- Data loading and exploration with Pandas
- Feature selection
- Training and testing a Machine Learning model
- Linear Regression
- Model evaluation using MAE
- Data visualization using Matplotlib

## 🚀 Future Improvements
- Use a larger, real-world dataset.
- Compare multiple Machine Learning algorithms.
- Improve model evaluation.
- Build a simple web interface for predictions.

## 👨‍💻 Author
CSE Student | Beginner Machine Learning Project
