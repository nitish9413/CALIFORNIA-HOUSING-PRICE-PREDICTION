from typing import List
from setuptools import setup

PROJECT_NAME="Housing-price-predictor"
VERSION="0.0.1"
AUTHOR="NITISH KATKADE"
DESCRIPTION="This is a 1st End-To-End Project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirements 
    mentioned in requirements.txt files

    return this function is going to return a list which contain name 
    of libraries in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readline()



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_require=get_requirements_list()
)