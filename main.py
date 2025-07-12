import json
import sys

from utils import *

show_banner()

def add(input_as_list):
      task_description = get_description(input_as_list)
      
      print("Task Description: ", task_description)

def main():
  while True:
    user_input: str = input("task-cli > ")
    input_as_list = user_input.split(" ")
    print(input_as_list)
    command = input_as_list[0]
    
    print("The command is: ", command)
    
    if command in ["exit", "0"]:
      print("Goodbye!")
      sys.exit()
    elif command == "add":  
      add(input_as_list)
        
      with open("tasks.json", "r") as f:
        content = json.load(f)
        print("Content:", content)

main()
