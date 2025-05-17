# 💳 Credit Card Fraud Detection

A web-based application built with Streamlit to detect fraudulent credit card transactions using machine learning. The app includes features for single prediction and bulk file upload.



## 📂 Project Structure

    ```
    Detect_Wise/
    │
    ├── views/                  
    │   ├── home.py            
    │   ├── prediction.py       
    │   └── bulk_prediction.py 
    ├──models
    |   ├── fraud_model.joblib      
    │   └── scaler.pkl
    ├── LICENSE
    ├── README.md
    ├── app.py
    ├── logo.png     
    └── requirements.txt             




## 🚀 Features

- Streamlit web app with custom navigation (`streamlit-option-menu`)
- Predict fraud for a single transaction
- Upload CSV file for batch prediction
- Modular code structure (one Python file per page)



## 🛠️ Setup Instructions

### 1. Clone the Repository
    ```
    git clone https://github.com/your-username/Credit_Card_Fraud_Detection.git
    cd Credit_Card_Fraud_Detection

### 2. Create a Virtual Environment
    ```
    python -m venv cenv

### 3. Activate the Environment
    ```
    .\cenv\Scripts\activate

### 4. Install Dependencies
    ```
    pip install -r requirements.txt


### 5. Run the App
streamlit run main.py


## 🧪 Model Info
The ML model used in this app is trained on the Kaggle Credit Card Fraud Detection Dataset. It uses features like transaction amount, time, and anonymized inputs (V1–V28).


## 🤝 Contributing

Contributions are welcome! Whether it's bug fixes, improvements, documentation updates, or new features — your help is appreciated.

### To contribute:

### 1. Fork the repository
### 2. Create a new branch:
     ```
     git checkout -b feature/your-feature-name
### Make your changes and commit:
      ```
    git commit -m "Add your message here"
### Push to your forked repo:
    ```
    git push origin feature/your-feature-name
   Open a Pull Request and describe your changes

## 📌 Guidelines
- Keep code clean and well-documented

- Write descriptive commit messages

- Try to maintain consistency with existing code style

- Always test your changes before submitting

## 📃 License

This project is licensed under the MIT License.



