# Paris Airbnb listings price explorer & predictor

**🏠 Interactive Streamlit app for exploring Airbnb listings in Paris and predicting listing prices.**  

The app allows users to:

- Visualize the **average price per neighborhood** on a map with a color gradient.
- Predict the **price of a listing** based on number of bedrooms and neighborhood, using a trained pipeline.

---

## Table of Contents

1. [Features](#features)  
2. [Installation](#installation)  
3. [Running Locally](#running-locally)  
4. [Testing](#testing)  
5. [Docker Usage](#docker-usage)  
6. [Usage](#usage)  
7. [Credits](#credits)  

---

## Features

- Interactive **Pydeck map** of Paris neighborhoods colored by average Airbnb price.  
- **Monthly average price line chart**.  
- **Dynamic price prediction** using a linear regression pipeline with preprocessing.  
- Handles missing data automatically.  
- Optional Docker setup for containerized deployment.  

## Project structure 
```text
airbnb-paris-app/
├── app.py                     # Streamlit app
├── train.py                   # Script to train the model
├── model_utils.py             # Training and prediction utilities
├── data_utils.py              # Data loading/cleaning functions
├── tests/
│   ├── test_data_utils.py     # Unit tests for data utilities
│   └── test_model_utils.py    # Unit tests for model utilities
├── data/
│   └── listings.csv           # Airbnb listings dataset
├── models/                    # Saved model pipelines (optional)
├── requirements.txt           # Python dependencies
├── environment.yml            # Conda environment file
├── Dockerfile                 # Docker setup
├── .gitignore                 # Git ignore file
├── .github/
│   └── workflows/
│       └── ci.yml             # Continuous Integration workflow
└── README.md
```
## Installation

1. Clone the repository:

```bash
git clone https://github.com/sofiacasalini/airbnb-paris-app.git
cd airbnb-paris-app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```
3. Install dependecies:
```bash
pip install -r requirements.txt
```

## Running locally
Run the Streamlit app:
```bash
streamlit run app.py
```

- Open http://localhost:8501 in your browser.
- The app will load the dataset and display the chart and predictor.

## Testing
Run tests with ```pytest```:
```bash
python -m pytest
```

## Docker usage
### Build Docker image
```bash
docker build -t airbnb-paris-app .
```

### Run the container
```bash
docker run -p 8501:8501 airbnb-paris-app
```

## Push to Docker Hub
#### 1. Log in
```bash
docker login
```
#### 2. Tag the image
```bash
docker tag airbnb-paris-app your-dockerhub-username/airbnb-paris-app:latest
```
#### 3. Push to Docker Hub
```bash
docker push your-dockerhub-username/airbnb-paris-app:latest
```
#### 4. Pull and run anywhere
```bash
docker pull your-dockerhub-username/airbnb-paris-app:latest  
docker run -p 8501:8501 your-dockerhub-username/airbnb-paris-app:latest
```
