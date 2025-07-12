WELCOME_MSG: str = ( 
      "Welcome to Task Tracker CLI\n"
      "Type 'help' to see all commands"
)


def show_banner(width: int = 40) -> None:
  print("".center(width, "-")) # e.g. -----------
  
  for line in WELCOME_MSG.splitlines(): # Make a list of welcome strings
    print(line.center(width, " ")) # Print lines with " " padding
    
  print("".center(width, "-")) # e.g. -----------
