'''
This file is for data cleaning and feature engineering
'''

import sys
import os
import numpy as np
import pandas as pd 
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging