import json
import sys

from utils import show_banner

show_banner()

def add(input_as_list):
      task_description_as_list = input_as_list[1:] # Exclude the command (which is at index 0) and keep everything
      task_description = " ".join(task_description_as_list) # Join the whole list and make a string
      
      if task_description.startswith('"') and task_description.endswith('"'): # Check if the description already has quotations
           task_description = task_description[1:-1] # if it already has quotaions marks, it removes it so that we can store it without quotes inside a string
           
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
