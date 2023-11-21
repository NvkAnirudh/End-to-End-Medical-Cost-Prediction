import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class PreditctPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path = os.path.join("artifacts","preprocessor.pkl")

            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)

            print(model)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e, sys)
        
# numerical_features = ['children']
#             categorical_features = ['age_range', 'bmi_range', 'sex', 'smoker', 'region']
class InputData:
    def __init__(self,
        age: int,
        children: int,
        bmi: float,
        sex: str,
        smoker: str,
        region: str):

        self.age = age
        self.children = children
        self.bmi = bmi
        self.sex = sex
        self.smoker = smoker
        self.region = region

    def get_data_as_dataFrame(self):
        try:
            input_dict = {
                "age": [self.age],
                "children": [self.children],
                "bmi": [self.bmi],
                "sex": [self.sex],
                "smoker": [self.smoker],
                "region": [self.region]
            }

            convert_dict = {
                'age': int,
                'children': int,
                'bmi': float,
                'sex': str,
                'smoker': str,
                'region': str
            }

            df = pd.DataFrame(input_dict)

            df = df.astype(convert_dict)
            print(df.info())

            # Adding an age_range categorical column where ages between 0-30 are considered 'young', 31-60 are considered 'middle-aged', and 61-100 are considered as 'old'
            df['age_range'] = 'old'
            df.loc[(df['age'] > 0) & (df['age'] <= 30), 'age_range'] = 'young'
            df.loc[(df['age'] > 30) & (df['age'] <= 60), 'age_range'] = 'middle-aged'

            # Adding a bmi_range categorical column where bmi <18.5 falls under underweight range, 18.5 - 24.9 falls under normal range, 25.0 - 29.9 falls under overweight range, and >30.0 falls under obese range
            df['bmi_range'] = 'normal'
            df.loc[(df['bmi'] < 18.5), 'bmi_range'] = 'underweight'
            df.loc[(df['bmi'] > 25.0) & (df['bmi'] < 29.9), 'bmi_range'] = 'overweight'
            df.loc[(df['bmi'] > 30.0), 'bmi_range'] = 'obese'

            return df

        except Exception as e:
            raise CustomException(e, sys)