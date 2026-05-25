import joblib
import pandas as pd

# import warnings
# warnings.filterwarnings('ignore')

model = joblib.load("diabetes.pkl")

columns = [
    "preg", "plas", "pres", "skin",
    "test", "mass", "pedi", "age"
]

data = pd.DataFrame(
    [[1, 1, 1, 1, 1, 1, 1, 1]],
    columns=columns
)

res = model.predict(data)

print(res)