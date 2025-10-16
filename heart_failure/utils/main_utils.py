import os
import sys

import pandas as pd
import numpy as np
import dill

from heart_failure.exception import HeartFailureException
from heart_failure.logger import logging


def save_object(file_path: str, object: object):
    """
    Saves object to file.

    Args:
        file_path (str): File location to be saved.
        object (object): Object file saved.
    """
    logging.info("Entered save_object method of utils.")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_object:
            dill.dump(object, file_object)
        logging.info("Exited save_object method of utils.")
    except Exception as e:
        raise HeartFailureException(e, sys) from e

def load_object(file_path: str) -> object:
    """
    Loads object from file.

    Args:
        file_path (str): File location to be loaded.

    Returns:
        object: Object file loaded.
    """
    logging.info("Entered load_object method of utils.")
    try:
        with open(file_path, "rb") as file_object:
            return np.load(file_object)
        logging.info("Exited load_object method of utils.")
    
    except Exception as e:
        raise HeartFailureException(e, sys) from e
    
def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Saves numpy array data to file.

    Args:
        file_path (str): File location to be saved.
        array (np.array): Array data saved.
    """
    logging.info("Entered save_numpy_array_data method of utils.")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_object:
            np.save(array, file_object)
        logging.info("Exited save_numpy_array_data method of utils.")
        
    except Exception as e:
        raise HeartFailureException(e, sys) from e

def load_numpy_array_data(file_path: str) -> np.array:
    """
    Loads numpy array data from file.

    Args:
        file_path (str): File location to be loaded.

    Returns:
        np.array: Array data loaded.
    """
    logging.info("Entered load_numpy_array_data method of utils.")
    try:
        with open(file_path, "rb") as file_object:
            return np.load(file_object)
        logging.info("Exited load_numpy_array_data method of utils.")
        
    except Exception as e:
        raise HeartFailureException(e, sys) from e