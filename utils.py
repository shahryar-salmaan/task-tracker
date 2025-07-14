import json
import os

WELCOME_MSG: str = ( 
      "Welcome to Task Tracker CLI\n"
      "Type 'help' to see all commands"
)


def show_banner(width: int = 40) -> None:
  print("".center(width, "-")) # e.g. -----------
  
  for line in WELCOME_MSG.splitlines(): # Make a list of welcome strings
    print(line.center(width, " ")) # Print lines with " " padding
    
  print("".center(width, "-")) # e.g. -----------
  
  
def get_description(input_as_list):
      task_description_as_list = input_as_list[1:] # Exclude the command (which is at index 0) and keep everything
      task_description = " ".join(task_description_as_list) # Join the whole list and make a string
      
      if task_description.startswith('"') and task_description.endswith('"'): # Check if the description already has quotations
           task_description = task_description[1:-1] # if it already has quotaions marks, it removes it so that we can store it without quotes inside a string
      
      return task_description
      
def read():
    if os.path.getsize("tasks.json") == 0:
          return []
          
    with open("tasks.json", "r") as f:
          content = json.load(f)
          return content
          
def generate_id():
  
    tasks = read()
    
    if not tasks:
      return 1
    else:
      max_id = max(int(task["id"]) for task in tasks)
      return max_id + 1
