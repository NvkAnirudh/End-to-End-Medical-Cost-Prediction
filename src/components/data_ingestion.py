import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Trainer

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw_data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Started data ingestion component")
        try:
            df = pd.read_csv("notebook/data/insurance.csv")  

            logging.info("Read the required data as pandas dataframe")

            # Dropping duplicates
            df.drop_duplicates(inplace=True)

            # Adding an age_range categorical column where ages between 0-30 are considered 'young', 31-60 are considered 'middle-aged', and 61-100 are considered as 'old'
            df['age_range'] = 'old'
            df.loc[(df['age'] > 0) & (df['age'] <= 30), 'age_range'] = 'young'
            df.loc[(df['age'] > 30) & (df['age'] <= 60), 'age_range'] = 'middle-aged'

            # Adding a bmi_range categorical column where bmi <18.5 falls under underweight range, 18.5 - 24.9 falls under normal range, 25.0 - 29.9 falls under overweight range, and >30.0 falls under obese range
            df['bmi_range'] = 'normal'
            df.loc[(df['bmi'] < 18.5), 'bmi_range'] = 'underweight'
            df.loc[(df['bmi'] > 25.0) & (df['bmi'] < 29.9), 'bmi_range'] = 'overweight'
            df.loc[(df['bmi'] > 30.0), 'bmi_range'] = 'obese'

            logging.info("Applied necessary data cleaning and feature engineering techniques")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Initiating train test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    di = DataIngestion()
    train_path, test_path = di.initiate_data_ingestion()

    # Performing DataTransformation
    dt = DataTransformation()
    train_arr, test_arr, _ = dt.initiate_data_transformation(train_path, test_path)
    print(train_arr.shape)

    # Model Training
    model_trainer = Trainer()
    r2_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
    print(r2_score)
