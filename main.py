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
  user_input: str = input("Say hello > ")
  print(user_input)
