import os
import sys

import numpy as np
import pandas as pd
from src.entity.config_entity import USvisaPredictorConfig
from src.entity.s3_estimator import USvisaEstimator
from src.exception import USvisaException
from src.logger import logging
from src.utils.main_utils import read_yaml_file
from pandas import DataFrame


class USvisaData:
    def __init__(self,
                Age,
                Gender,
                Social_Media_Hours,
                Exercise_Hours,
                Sleep_Hours,
                Screen_Time_Hours,
                Survey_Stress_Score,
                Wearable_Stress_Score,
                Academic_Performance
                ):
        """
        Usvisa Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.Age = Age
            self.Gender = Gender
            self.Social_Media_Hours = Social_Media_Hours
            self.Exercise_Hours = Exercise_Hours
            self.Sleep_Hours = Sleep_Hours
            self.Screen_Time_Hours = Screen_Time_Hours
            self.Survey_Stress_Score = Survey_Stress_Score
            self.Wearable_Stress_Score = Wearable_Stress_Score
            self.Academic_Performance = Academic_Performance


        except Exception as e:
            raise USvisaException(e, sys) from e

    def get_usvisa_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            usvisa_input_dict = self.get_usvisa_data_as_dict()
            return DataFrame(usvisa_input_dict)
        
        except Exception as e:
            raise USvisaException(e, sys) from e


    def get_usvisa_data_as_dict(self):
        """
        This function returns a dictionary from USvisaData class input 
        """
        logging.info("Entered get_usvisa_data_as_dict method as USvisaData class")

        try:
            input_data = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Social_Media_Hours": [self.Social_Media_Hours],
                "Exercise_Hours": [self.Exercise_Hours],
                "Sleep_Hours": [self.Sleep_Hours],
                "Screen_Time_Hours": [self.Screen_Time_Hours],
                "Survey_Stress_Score": [self.Survey_Stress_Score],
                "Wearable_Stress_Score": [self.Wearable_Stress_Score],
                "Academic_Performance": [self.Academic_Performance],
            }

            logging.info("Created usvisa data dict")

            logging.info("Exited get_usvisa_data_as_dict method as USvisaData class")

            return input_data

        except Exception as e:
            raise USvisaException(e, sys) from e

class USvisaClassifier:
    def __init__(self,prediction_pipeline_config: USvisaPredictorConfig = USvisaPredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            # self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise USvisaException(e, sys)


    def predict(self, dataframe) -> str:
        """
        This is the method of USvisaClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of USvisaClassifier class")
            model = USvisaEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise USvisaException(e, sys)