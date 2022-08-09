from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataTransformationConfig


class DataTransformation:

    def __init__(self,data_trnasformation_config: DataTransformationConfig,
                 data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_artifact: DataValidationArtifact   
                ):
                
        pass