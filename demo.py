from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.pipeline.pipeline import Pipeline
from housing.components.data_transformation import DataTransformation
#from housing.util.util import load_data

def main():
    try:
        # pipeline =Pipeline()
        # pipeline.run_pipeline()
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)

        schema_f = r"C:\Users\nitis\INeuron\Projects\Project_1\Machine_Learning_Project\config\schema.yaml"
        file_p = r"C:\Users\nitis\INeuron\Projects\Project_1\Machine_Learning_Project\housing\artifact\data_ingestion\2022-08-08-15-02-14\ingested_data\train\housing.csv"


        df =DataTransformation.load_data(file_path=file_p,schema_file_path=schema_f)

        print(df.columns)
        print(df.dtypes)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()