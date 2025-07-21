import json
import sys

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

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
    new_input = input_as_list[1:]
    task_description = get_description(new_input)
    updatedAt = get_time("utc")
     
    id = new_input[0]
    
    print(id)
    print(task_description)
    tasks = read()
    
    for task in tasks:
      if task["id"] == id:
       
       task["description"] = task_description
       task["updatedAt"] = updatedAt
       write(tasks)
       print(f"Task updated successfully (ID: {id})")
      

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
    else:
      print(f"{command}? That command isn't available.")

def list_tasks():
  tasks = read()
  
  for task in tasks:
    print(task["id"], task["description"], task["status"])
    
list_tasks()

sample_data = {
  "id": "1",
  "description": "Finish writing the blog post on JSON in Python",
  "status": "in-progress",
  "createdAt": "2025-07-12T14:30:00Z",
  "updatedAt": "2025-07-12T16:00:00Z"
}


"""
dict_obj = read()
dict_obj.append(sample_data)

print(dict_obj)
write(dict_obj)

content.append(sample_data)

with open("tasks.json", "w") as f:
  json.dump(content, f, indent=4)

print(content)
    """
