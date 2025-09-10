from Networksecurity.Components.data_ingestion import DataIngestion
#from Networksecurity.Components.data_validation import DataValidation
#from Networksecurity.Components.data_transformation import DataTransformation
from Networksecurity.Exception.exception import NetworkSecurityException
from Networksecurity.Logging.logger import logging
from Networksecurity.Entity.config_entity import DataIngestionConfig
from Networksecurity.Entity.config_entity import TrainingPipelineConfig

#from Networksecurity.Components.model_trainer import ModelTrainer
#from Networksecurity.Entity.config_entity import ModelTrainerConfig
 

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
       
        
    except Exception as e:
           raise NetworkSecurityException(e,sys)
