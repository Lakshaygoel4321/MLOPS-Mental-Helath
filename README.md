# 🧠 Student Mental Health Analysis

Project Overview

This project focuses on analyzing student mental health and stress levels. It involves data ingestion, validation, transformation, and model training, along with a web application for local deployment. The project utilizes MongoDB for database management and follows a structured pipeline for processing and analysis.

# Project Workflow

## 1. Setting Up the Project

Run template.py to create the project template.

Configure setup.py and pyproject.toml to import local packages.

Create a virtual environment and install dependencies:

Verify installed packages:

## 2. MongoDB Setup

Sign up on MongoDB Atlas and create a project.

Create a cluster using the M0 free tier.

Set up a database user with a username and password.

Allow access from all IP addresses (0.0.0.0/0).

Get the connection string (Python 3.6 or later), replace <password>, and save it.

Create a notebook folder and add mongoDB_demo.ipynb.

Load and push the dataset to MongoDB from the notebook.

Verify the data in MongoDB Atlas under "Browse Collections."

## 3. Logging, Exception Handling, and Notebooks

Implement logging in logger.py and test with demo.py.

Implement exception handling in exception.py and test with demo.py.

Perform EDA and Feature Engineering.

## 4. Data Ingestion

Define connection variables in constants.__init__.py.

Configure mongo_db_connections.py for database connectivity.

Implement data fetching and transformation in data_access.

Define data ingestion configurations in config_entity.py.

Create DataIngestionArtifact in artifact_entity.py.

Develop data_ingestion.py for data loading.

Run demo.py after setting up the MongoDB URL:

## 5. Data Validation, Transformation & Model Training

Implement utilities in utils.main_utils.py.

Define schema details in config.schema.yaml.

Develop:

Data Validation component.

Data Transformation component (estimator.py in entity folder).

Model Training component (estimator.py in entity folder).

## 6. Model Evaluation & Model Pusher

Implement model evaluation to assess performance.

Push the trained model to the local environment.

## 7. Web Application Setup

Create a templates and static folder.

Develop app.py for web interface.

Start the app on localhost:

Access the app at http://127.0.0.1:5000/.

Future Enhancements

Cloud deployment using CI/CD.

Integration with additional mental health datasets.

## Conclusion

This project provides insights into student mental health trends and offers a structured approach to data processing and model training for predictive analysis. The application is currently available for local use and can be extended for broader deployment in the future.

