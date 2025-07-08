WELCOME_MSG: str = ( 
      "Welcome to Task Tracker CLI\n"
      "Type 'help' to see all commands"
)

width: int = 40

print("".center(width, "-"))

for line in WELCOME_MSG.splitlines():

  print(line.center(width, " "))

print("".center(width, "-"))

while True:
  user_input: str = input("task-cli > ")
  input_as_list = user_input.split(" ")
  print(input_as_list)
  command = input_as_list[0]
  
  print(command)
  
  if command == "add":
    task_description_as_list = input_as_list[1:]
    task_description = " ".join(task_description_as_list)
    
    if task_description.startswith('"') and task_description.endswith('"'):
         task_description = task_description[1:-1]
         
    print(task_description)
    
    id = None
    status = None
    
    task_dict = { "id": id,
                  "status": status,
                  "description": task_description }
                  
    print(task_dict)
