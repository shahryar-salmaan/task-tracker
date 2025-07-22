import json
import sys

from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

from utils import *

show_banner()

def get_input():
    user_input: str = input("task-cli > ").lower().strip()
    input_as_list = user_input.split(" ")
    
    return input_as_list
  

def add(input_as_list):
      id = generate_id()
      task_description = get_description(input_as_list)
      status = "in-progress"
      createdAt = get_time("utc")
      updatedAt = None
      
      task = {"id": f"{id}",
              "description": task_description,
              "status": status,
              "createdAt": createdAt,
              "updatedAt": updatedAt
      }
      
      tasks = read()
      
      tasks.append(task)
      
      write(tasks)
      
      print(f"Task added successfully (ID: {id})")
      
      
def update(input_as_list):
  try:
        new_input = input_as_list[1:]
        task_description = get_description(new_input)
        updatedAt = get_time("utc")
        id = new_input[0]
        
        if task_description == "":
          print("Please provide a task description.")
          return
        tasks = read()
        
        for task in tasks:
          if task["id"] == id:
           
           task["description"] = task_description
           task["updatedAt"] = updatedAt
           write(tasks)
           print(f"Task updated successfully (ID: {id})")
  except:
    print("Invalid input. Example: update [task-id] [task-description]")

def delete(input_as_list):
  
  tasks = read()
  
  id = input_as_list[1]
  
  index_to_del = None
  
  for index, task in enumerate(tasks):
    if task["id"] == id:
      index_to_del = index
      break
    
  del tasks[index_to_del]
  write(tasks)
  print(f"Task deleted successfully (ID: {id})")


def mark(input_as_list):
  
  tasks = read()
  id = input_as_list[1]
  
  target_id = None
  
  for index, task in enumerate(tasks):
    if task["id"] == id:
      target_id = index
      break
    
  if input_as_list[0] == "mark-in-progress":
    tasks[target_id]["status"] = "in-progress"
  elif input_as_list[0] == "mark-done":
    tasks[target_id]["status"] = "done"
    
  write(tasks)
  print(f"Task marked successfully (ID: {id})")


def list_tasks(input_as_list):
  tasks = read()
  print("".center(40, "-"))
  if len(input_as_list) > 1: 
    if input_as_list[0] == "list" and input_as_list[1] == "done":
      for task in tasks:
        if task["status"] == "done":
          print(task["id"] + ".", task["description"].capitalize(),"-", task["status"].capitalize())
    elif input_as_list[0] == "list" and input_as_list[1] == "todo" or "in-progress":
      for task in tasks:
        if task["status"] == "in-progress":
          print(task["id"] + ".", task["description"].capitalize(),"-", task["status"].capitalize())
  elif input_as_list[0] == "list":
      for task in tasks:
        print(task["id"] + ".", task["description"].capitalize(),"-", task["status"].capitalize())
  print("".center(40, "-"))
  
if not Path("tasks.json").exists():
  with open("tasks.json", "w") as f:
    json.dump([], f)

def main():
  while True:
    input_as_list = get_input()
    command = input_as_list[0]
    
    if command in ["exit", "0"]:
      print("Goodbye!")
      sys.exit()
    elif command == "add":  
      add(input_as_list)
    elif command == "update":
      update(input_as_list)
    elif command == "delete":
      delete(input_as_list)
    elif command.startswith("mark"):
      mark(input_as_list)
    elif command == "list":
      list_tasks(input_as_list)
    else:
      print(f"{command}? That command isn't available.")
      

if __name__ == "__main__":
  main()
