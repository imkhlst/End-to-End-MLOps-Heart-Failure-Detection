import os
import sys


def error_message_detail(error, error_detail: str):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occured python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    )
    return error_message

class HeartFailureException(Exception):
    def __init__(self, error_message: str, error_detail):
        """_summary_

        Args:
            error_message (str): _description_
            error_detail (_type_): _description_
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )
    
    def __str__(self):
        return self.error_message