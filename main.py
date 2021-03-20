# This is a script to auto detect OS and set system wide proxy
import sys
import platform
from rich.console import Console
from art import *

console = Console()

os = platform.system()

tprint("Set Proxy")

if os == "Windows":
    console.print("Sorry, this script is not made to use with Windows !", style="bold red")

elif os == "Linux":
    print("- Detected Linux based OS")

else:
    print("Could not detect OS")
    print("\nExit")
    sys.exit()
