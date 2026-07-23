import json
import csv
import pickle
import sys
import os
from typing import Any

app_args = sys.argv
pwd = os.getcwd()
input_file = app_args[1] 
output_file = app_args[2]
changes_to_do = app_args[3:]

def converter_app():
    data_types = ["csv", "pickle", "json", "txt"]
    input_type = input_file.split(".")
    input_type = input_type[-1]
    output_type = output_file.split(".")
    output_type = output_type[-1]
    if not input_type  in data_types or not output_type in data_types:
        raise ValueError("Incorrect type of data choosen. Available data types for converter: JSON, TXT, CSV and PICKLE.")
    elif input_type == output_type:
        raise ValueError("The same type of data to convert were choosen. Data types have to be different of each other.")
    else:
        pass

class BaseHandler():
  
    def __init__(self, input_file, output_file, changes_to_do) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.changes_to_do = changes_to_do

    def __repr__(self) -> str:
        return f"[INFO] In file: {self.input_file} | Out file: {self.output_file}\n" \
        f"[INFO] Changes to do: {self.changes_to_do}"



class HandlerToTXT(BaseHandler):
    @classmethod
    def open_item(cls): 
        with open(f"{pwd}/{output_file}", mode="r", encoding="UTF-8") as f:
            input_content = f.read()



    @classmethod
    def save_item(cls): 
        with open(f"{pwd}/{output_file}", mode="w", encoding="UTF-8") as f:
            f.write(input_content)




converter_app()







