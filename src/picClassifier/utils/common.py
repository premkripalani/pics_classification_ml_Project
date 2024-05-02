#Project constants 

#import all libraries

import os
from box.exceptions import Boxvalueerror
import yaml
from picClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# Reading YAML files
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input

    Raises:
        valueError: if yaml files is empty 
        e: empty file
    
    Returns:
        ConfigBox: ConfigBox type
           
    """

    try: 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Boxvalueerror:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

# Create Project Directories for ex Artifacts

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list) : list of path of directories
        ignore_log(bool, optional): ignore if multiple directories are created. Defaults to False.
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")