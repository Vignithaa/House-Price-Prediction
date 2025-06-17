# 🏠 House Price Prediction using Machine Learning

This project predicts Boston house prices using various regression models such as Linear Regression, Lasso, and Random Forest.

## 📊 Dataset
- **Source:** scikit-learn's Boston Housing dataset (converted to CSV)
- Features: crime rate, number of rooms, property tax, etc.

## 🚀 Tech Used
- Python
- Pandas, Numpy
- Scikit-learn
- Matplotlib, Seaborn

## 📈 Models Used
- Linear Regression
- Lasso Regression
- Random Forest Regressor

## 📁 Project Structure
- `notebooks/`: Jupyter notebooks for EDA and model building
- `model/`: Trained model saved with pickle
- `app.py`: Streamlit interface (optional)
- `requirements.txt`: Dependencies

## 🏃‍♂️ Run the Project
```bash
pip install -r requirements.txt
jupyter notebook notebooks/house_price_prediction.ipynb
```

## 📦 Deployment
- Run `streamlit run app.py` to launch the web app (optional)
