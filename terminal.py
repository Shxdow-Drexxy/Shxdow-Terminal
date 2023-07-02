import datetime
import os
import shutil
import platform
import psutil
import netifaces
from colorama import init, Fore
import time
import random
import subprocess
import math
import curses

# Initialize Colorama
init()
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW

# Available commands
commands = {
    "hack": "Perform hacking sequence",
    "help": "Display available commands",
    "echo": "Repeat anything after the word 'echo'",
    "exit": "Exit the program",
    "data": "Show current time, user, drives, and network information",
    "clear": "Clear the console",
    "generate": "Generate a random number",
    "sleep": "Pause the program for a specified number of seconds",
    "files": "List files in the current directory",
    "3d": "Animate 3 different text messages",
}

# Different colors for formatting
system_info_color = Fore.CYAN
heading_color = Fore.YELLOW
data_color = Fore.GREEN
error_color = Fore.RED
highlight_color = Fore.BLUE


def perform_hacking_sequence():
    tasks = [
        "Initializing the hacking sequence...",
        "Accessing mainframe...",
        "Bypassing firewall...",
        "Cracking encryption...",
        "Gaining root access...",
        "Downloading sensitive data...",
        "Almost there...",
    ]

    for i, task in enumerate(tasks):
        time.sleep(random.uniform(0.1, 1))

        # Print the completion status in green
        print(green + "completed " + task)


def display_help():
    print("Available commands:")
    for command, description in commands.items():
        print(f"{command}: {description}")


def repeat_echo(text):
    echo_text = text.strip()[5:]
    print(highlight_color + echo_text)


def get_hardware_id():
    try:
        output = subprocess.check_output("wmic csproduct get uuid").decode().strip()
        return output.split("\n")[-1]
    except Exception:
        return "Unknown HWID"


def get_os_version():
    return f"{platform.system()} {platform.release()} ({platform.architecture()[0]})"


def get_memory_info():
    mem = psutil.virtual_memory()
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    available = round(mem.available / (1024 * 1024 * 1024), 2)
    return f"Total Memory: {total}GB, Available Memory: {available}GB"


def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    total_gb = round(total / (1024**3), 2)
    used_gb = round(used / (1024**3), 2)
    free_gb = round(free / (1024**3), 2)
    return f"Total Disk Space: {total_gb}GB, Used: {used_gb}GB, Free: {free_gb}GB"


def get_network_interfaces():
    interfaces = netifaces.interfaces()
    interface_info = []
    for interface in interfaces:
        ifaddresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in ifaddresses:
            ip = ifaddresses[netifaces.AF_INET][0]['addr']
            mac = ifaddresses[netifaces.AF_LINK][0]['addr']
            interface_info.append(f"{interface}: IP - {ip}, MAC - {mac}")
    return "\n".join(interface_info)


def display_data():
    now = datetime.datetime.now()
    username = os.getlogin()
    drives = ", ".join(os.listdir("/"))
    hwid = get_hardware_id()
    os_version = get_os_version()
    memory_info = get_memory_info()
    disk_usage = get_disk_usage()
    network_interfaces = get_network_interfaces()

    # System information
    print(system_info_color + "[System Information]")
    print()

    # Current time
    print(f"{highlight_color}Current time: {now}")

    # User
    print(f"{highlight_color}User: {username}")

    # Hardware ID
    print(f"{highlight_color}Hardware ID: {hwid}")

    # Operating System
    print(f"{highlight_color}Operating System: {os_version}")
    print()

    # Computer Specifications
    print(heading_color + "[Computer Specifications]")

    # Memory
    print(f"{highlight_color}Memory: {memory_info}")

    # Disk Usage
    print(f"{highlight_color}Disk Usage: {disk_usage}")
    print()

    # Drives and Network
    print(heading_color + "[Drives and Network]")

    # Folders in current directory
    print(f"{highlight_color}Folders in current directory: {drives}")
    print()

    # Network Interfaces
    print(heading_color + "[Network Interfaces]")
    print(network_interfaces)


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def generate_random_number():
    number = random.randint(1, 100)
    print(f"{highlight_color}Random number: {number}")


def pause_program():
    seconds = lambda: input("Enter the number of seconds to pause: ")
    try:
        seconds = float(seconds())
        time.sleep(seconds)
        print(f"{highlight_color}Paused for {seconds} seconds.")
    except ValueError:
        print(f"{error_color}Invalid input. Please enter a valid number of seconds.")


def list_files():
    files = os.listdir()
    print("Files in the current directory:")
    for file in files:
        print(file)


def animate_3d(stdscr):
    # Disable cursor blinking
    curses.curs_set(0)

    # Define donut parameters
    donut_radius = 10
    donut_height = 3

    # Get terminal size
    height, width = stdscr.getmaxyx()

    theta = 0.0
    while True:
        stdscr.clear()

        # Generate donut coordinates
        theta_spacing = 0.07
        phi_spacing = 0.02

        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        phi = 0.0
        while phi < math.pi * 2:
            cos_phi = math.cos(phi)
            sin_phi = math.sin(phi)

            x = cos_theta * (donut_radius + cos_phi * donut_height)
            y = sin_theta * (donut_radius + cos_phi * donut_height)
            z = sin_phi * donut_height + donut_height

            donut_2d_x = int((width / 2) + x * 2)
            donut_2d_y = int((height / 2) + y)

            if 0 <= donut_2d_x < width and 0 <= donut_2d_y < height:
                stdscr.addstr(donut_2d_y, donut_2d_x, '#')

            phi += phi_spacing

        stdscr.refresh()
        time.sleep(0.1)  # Modify animation speed here

        # Increment theta to make the donut spin
        theta += theta_spacing


def main():
    while True:
        input_color = Fore.GREEN
        action_color = Fore.RED
        command = input(f"{input_color}Enter a command: ")

        if command == "hack":
            print(action_color + "Performing hacking sequence...")
            perform_hacking_sequence()
        elif command == "help":
            display_help()
        elif command.startswith("echo"):
            repeat_echo(command)
        elif command == "exit":
            print(action_color + "Exiting the program...")
            break
        elif command == "data":
            print(action_color + "Displaying system information...")
            display_data()
        elif command == "clear":
            clear_console()
        elif command == "generate":
            generate_random_number()
        elif command == "sleep":
            pause_program()
        elif command == "files":
            list_files()
        elif command == "3d":
            curses.wrapper(animate_3d)
        else:
            print(f"{error_color}Invalid command. Enter 'help' for a list of available commands.")


if __name__ == "__main__":
    clear_console()
    logo_color = Fore.CYAN
    print(
        logo_color
        + r"""

   _____ _             _                 _                      _             _
  / ____| |           | |               | |                    (_)           | |
 | (___ | |__ __  ____| | _____      __ | |_ ___ _ __ _ __ ___  _ _ __   __ _| |
  \___ \| '_ \\ \/ / _` |/ _ \ \ /\ / / | __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
  ____) | | | |>  < (_| | (_) \ V  V /  | ||  __/ |  | | | | | | | | | | (_| | |
 |_____/|_| |_/_/\_\__,_|\___/ \_/\_/    \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|



          """
        + Fore.RESET
    )

    main()
