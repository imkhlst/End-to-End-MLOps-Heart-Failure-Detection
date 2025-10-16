import os
from datetime import date

database_name = "heart-failure"
collection_name = "heart"
mongo_db_url = "MONGODB_URL"

pipeline_name: str = "heartfailure"
artifact_dir: str = "artifact"

file_name: str = "heart.csv"
train_file_name: str = "train.csv"
test_file_name: str = "test.csv"

model_file_name: str = "model.pkl"
preprocessing_file_name: str = "preprocessing.pkl"

aws_access_key_id_env_key = "AWS_ACCESS_KEY_ID"
aws_secret_access_key_env_key = "AWS_SECRET_ACCESS_KEY"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
data_ingestion_collection_name: str = "heart"
data_ingestion_dir_name: str = "data_ingestion"
data_ingestion_feature_store_dir: str = "feature_store"
data_ingestion_ingested_dir: str = "ingested"