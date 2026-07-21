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

class BaseHandler():
  
    def __init__(self, input_file, output_file, changes_to_do) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.changes_to_do = changes_to_do

    def __repr__(self) -> str:
        return f"[INFO] In file: {self.input_file} | Out file: {self.output_file}\n" \
        f"[INFO] Changes to do: {self.changes_to_do}"
    @staticmethod
    def open_item(pwd=pwd):
        with open(f"{pwd}/{input_file}", mode="r", encoding="UTF-8") as f:
            
            f.write(input_file)


class HandlerToTXT(BaseHandler):

    @staticmethod
    def save_item(pwd = pwd): 
        with open(f"{pwd}/{output_file}", mode="w", encoding="UTF-8") as f:
            f.write(input_file)
        





main_instance = BaseHandler(input_file, output_file, changes_to_do)


print(main_instance)

test = HandlerToTXT.save_item()






