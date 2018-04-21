# TinyMenu 
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![HitCount](http://hits.dwyl.io/QiuDev/TinyMenu.svg)](http://hits.dwyl.io/QiuDev/TinyMenu) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama) [![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

TinyMenu is a simple yet effective utility to simplify and speed up the creation of customizable command-line menus in Python.
It is marked by its plain and basic functionality, leaving implementation details up to the developer.

## Usage
In order to use TinyMenu functionality the following import statement is required:
```py
import tinymenu
```
### Creating the menu
The code snippet below will create a basic command-line menu containg one command.
An explanation and other available attributes and functions are documented below.
```py
def handle_help_command(cmd, *args):
    """
    Function that is called when user enters 'help' command
    """
    print('You entered the help command!')

menu = tinymenu.TinyMenu()
menu.prompt = '$> '

command = tinymenu.Command('help', handle_help_command)
command.arg_limit = [0] # Don't allow any command arguments

menu.add_command(command)
menu.run()
```
```
Output:

$> help
You entered the help command!
```
#### ```TinyMenu```class:
- ```prompt``` (expects string) - Stores prompt to be displayed (e.g.: ```$>```  or ```~/home>```)
- ```interrupt_handler``` (expects method/function) - Stores method/function to be called on ```KeyboardInterrupt```
    - e.g.: ```def handle_interrupt()```
- ```unknown_command_handler``` (expects method/function) - Stores method/function to be called when an unknown command was entered
    - **1st** argument: entered command [```string```]
    - **2nd** argument: command arguments [```*string```]
    - **e.g.**: ```def handle_unknown_command(cmd, *cmd_arguments)```
- ```invalid_args_handler``` (expects method/function) - Stores method/function to be called when a command with invalid command arguments was entered
    - **1st** argument: entered command [```Command``` (see below)]
    - **2nd** argument command arguments [```string```]
    - **e.g.**: ```def handle_invalid_args(cmd, *cmd_arguments)```
- ```add_command(command)``` - Adds a command to the menu
    - **command** - ```Command``` (see below) to be added
- ```remove_command(command)``` - Removes a command from the menu
    - **command** - ```Command``` (see below) to be added
- ```run()``` - Starts the menu and listens for input

#### ```Command```class:
- ```__init__(command, handler)``` - Initialization of ```Command``` instance
- ```command``` (expects string) - Stores name of the command (string to be entered in menu)
- ```handler``` (expects method/function) - Stores method/function to be called when command entered
    - **1st** argument: entered command [```Command```]
    - **2nd** argument: command arguments [```*string```]
- ```arg_limit``` (expects list of integers) - Stores possible amounts of arguments (```None``` = no limit)

## Dependencies & Compatibility
TinyMenu does not have any dependencies and is compatible with Python 2 & Python 3
