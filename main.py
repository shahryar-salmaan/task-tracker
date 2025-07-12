WELCOME_MSG: str = ( 
      "Welcome to Task Tracker CLI\n"
      "Type 'help' to see all commands"
)

width: int = 40 # Width for padding

print("".center(width, "-")) # e.g. -----------

for line in WELCOME_MSG.splitlines(): # Make a list of welcome strings

  print(line.center(width, " ")) # Print lines with " " padding

print("".center(width, "-")) # e.g. -----------

while True:
  user_input: str = input("task-cli > ")
  input_as_list = user_input.split(" ")
  print(input_as_list)
  command = input_as_list[0]
  
  print("The command is: ", command)
  
  if command == "add":
    task_description_as_list = input_as_list[1:] # Exclude the command (which is at index 0) and keep everything
    task_description = " ".join(task_description_as_list) # Join the whole list and make a string
    
    if task_description.startswith('"') and task_description.endswith('"'): # Check if the description already has quotations
         task_description = task_description[1:-1] # if it already has quotaions marks, it removes it so that we can store it without quotes inside a string
         
    print("Task Description: ", task_description)
    
    id = None
    status = None
    
    task_dict = { "id": id,
                  "status": status,
                  "description": task_description }
                  
    print("Task Dictionary: ", task_dict)
