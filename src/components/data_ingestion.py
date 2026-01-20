import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # DataIngestionConfig Object created
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion Method or Component")
        try:
            # Code to insert data into dataframe from MongoDB, SQL, Local Source etc
            df = pd.read_csv(r"D:\Projects\Krish Naik ML Project\Notebook\data\stud.csv")
            logging.info('Read the dataset as dataframe successfully')

            # Artifacts directory create kar rahe hain agar nhi hai toh.
            # self.ingestion_config.train_data_path se path nikal kar directory banayi ja rahi hai.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Raw data ko artifacts folder mein save kar rahe hain.
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            # Data ko Train aur Test sets mein split kar rahe hain.
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Split huye data ko alag-alag CSV files mein save kar rahe hain.
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed successfully")

            # Agle components (Data Transformation) ke liye paths return kar rahe hain.
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # Agar kuch crash hua toh hamara CustomException trigger ho jayega.
            raise CustomException(e, sys)

# Testing code (Normally ye main.py se trigger hota hai)
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    