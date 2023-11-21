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
        children: str,
        bmi: float,
        sex: str,
        smoker: str,
        region: str,
        age_range: str,
        bmi_range: str):

        self.age = age
        self.children = children
        self.bmi = bmi
        self.sex = sex
        self.smoker = smoker
        self.region = region
        self.age_range = age_range
        self.bmi_range = bmi_range

    def get_data_as_dataFrame(self):
        try:
            input_dict = {
                "age": [self.age],
                "children": [self.children],
                "bmi": [self.bmi],
                "sex": [self.sex],
                "smoker": [self.smoker],
                "region": [self.region],
                "age_range": [self.age_range],
                "bmi_range": [self.bmi_range]
            }

            return pd.DataFrame(input_dict)

        except Exception as e:
            raise CustomException(e, sys)