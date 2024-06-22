# Flask Machine Learning Prediction App

This is a Flask web application is my learning end-to-end project with deployment that predicts outcomes of math scores of student based on user input using a machine learning pipeline. The application uses data from a form, processes it, and provides predictions.

## Features

- Web interface for user input
- Machine learning pipeline for making predictions
- Display of prediction results

## Installation

To run this application, you need to have Python installed. Follow the steps below to set up and run the application.

### Clone the Repository

```sh
git clone https://github.com/tinapyp/student-performance-aws-deployment.git
cd student-performance-aws-deployment
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:

    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://0.0.0.0:3000`.

## Project Structure

```
├──  app.py
├──  artifacts
│  ├──  data.csv
│  ├──  model.pkl
│  ├──  preprocessor.pkl
│  ├──  test.csv
│  └──  train.csv
├──  catboost_info
│  ├──  catboost_training.json
│  ├──  learn
│  │  └──  events.out.tfevents
│  ├──  learn_error.tsv
│  ├──  time_left.tsv
│  └──  tmp
├──  compose.yaml
├──  Dockerfile
├──  notebook
│  ├──  '1 . EDA STUDENT PERFORMANCE .ipynb'
│  ├──  '2. MODEL TRAINING.ipynb'
│  ├──  catboost_info
│  │  ├──  catboost_training.json
│  │  ├──  learn
│  │  │  └──  events.out.tfevents
│  │  ├──  learn_error.tsv
│  │  ├──  time_left.tsv
│  │  └──  tmp
│  └──  data
│     └──  stud.csv
├──  README.Docker.md
├──  README.md
├──  requirements.txt
├──  setup.py
├──  src
│  ├──  __init__.py
│  │  ├──  __init__.cpython-310.pyc
│  │  ├──  exception.cpython-310.pyc
│  │  ├──  logger.cpython-310.pyc
│  │  ├──  logger.cpython-312.pyc
│  │  └──  utils.cpython-310.pyc
│  ├──  components
│  │  ├──  __init__.py
│  │  │  ├──  __init__.cpython-310.pyc
│  │  │  ├──  data_transformation.cpython-310.pyc
│  │  │  └──  model_trainer.cpython-310.pyc
│  │  ├──  data_ingestion.py
│  │  ├──  data_transformation.py
│  │  └──  model_trainer.py
│  ├──  exception.py
│  ├──  logger.py
│  ├──  pipeline
│  │  ├──  __init__.py
│  │  │  ├──  __init__.cpython-310.pyc
│  │  │  └──  predict_pipeline.cpython-310.pyc
│  │  ├──  predict_pipeline.py
│  │  └──  train_pipeline.py
│  └──  utils.py
└──  templates
   ├──  home.html
   └──  index.html
```

## Usage

1. Navigate to the home page.
2. Enter the required data in the form.
3. Submit the form to receive predictions.

## Dependencies

- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn
- catboost
- xgboost
- flask
