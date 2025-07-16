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
      task_description = get_description(input_as_list)
      

def main():
  while True:
    input_as_list = get_input()
    command = input_as_list[0]
    
    if command in ["exit", "0"]:
      print("Goodbye!")
      sys.exit()
    elif command == "add":  
      add(input_as_list)
    else:
      print(f"{command}? That command isn't available.")

  
print(get_time("zulu"))
print(get_time("utc"))
print(get_time("bd"))

      
sample_data = {
  "id": "1",
  "description": "Finish writing the blog post on JSON in Python",
  "status": "in-progress",
  "createdAt": "2025-07-12T14:30:00Z",
  "updatedAt": "2025-07-12T16:00:00Z"
}
"""
content.append(sample_data)

with open("tasks.json", "w") as f:
  json.dump(content, f, indent=4)

print(content)
    """
