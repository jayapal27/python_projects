import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os


# Create folders
os.makedirs("model", exist_ok=True)
os.makedirs("output", exist_ok=True)

# Step 1: Load Kaggle dataset
data = pd.read_csv("data/House_Price_Prediction_Dataset.csv")



# Step 3: Encode categorical features
categorical_features = ["Location", "Condition", "Garage"]
data = pd.get_dummies(data, columns=categorical_features, drop_first=True)

# Step 4: Define features and target
X = data.drop("Price", axis=1)
y = data["Price"]

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Predict prices
y_pred = model.predict(X_test)

# Step 8: Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Step 9: Save trained model
joblib.dump(model, "model/linear_regression_model.pkl")

# Step 10: Save evaluation results
with open("output/model_evaluation.txt", "w") as f:
    f.write("Linear Regression Model Evaluation\n")
    f.write(f"Mean Absolute Error (MAE): {mae}\n")
    f.write(f"R2 Score: {r2}\n")

# Step 11: Save model visualization
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual House Price")
plt.ylabel("Predicted House Price")
plt.title("Linear Regression: Actual vs Predicted House Prices")
plt.savefig("output/linear_regression_model.png")
plt.close()

print("✅ Linear Regression Model Trained Successfully")
print("MAE:", mae)
print("R2 Score:", r2)
print("📊 Model image saved in output folder")
