# simple_msf_wrapper.py
A Simple wrapper to generate plain shellcode through msfvenom and for setting up a listener in msfconsole



./simple_msf_wrapper.py
  _____  _            _  _                   _        __          __                                                             
 / ____|| |          | || |                 | |       \ \        / /                                                             
| (___  | |__    ___ | || |  ___   ___    __| |  ___   \ \  /\  / /  _ __   __ _  _ __   _ __    ___  _ __                       
 \___ \ | '_ \  / _ \| || | / __| / _ \  / _` | / _ \   \ \/  \/ /  | '__| / _` || '_ \ | '_ \  / _ \| '__|                      
 ____) || | | ||  __/| || || (__ | (_) || (_| ||  __/    \  /\  /   | |   | (_| || |_) || |_) ||  __/| |                         
|_____/ |_| |_| \___||_||_| \___| \___/  \__,_| \___|     \/  \/    |_|    \__,_|| .__/ | .__/  \___||_|                         
                                                                                 | |    | |                                      
                                                                                 |_|    |_|                                      
 __  __        _                       _         _  _     ______                                                       _         
|  \/  |      | |                     | |       (_)| |   |  ____|                                                     | |        
| \  / |  ___ | |_   __ _  ___  _ __  | |  ___   _ | |_  | |__    _ __   __ _  _ __ ___    ___ __      __  ___   _ __ | | __     
| |\/| | / _ \| __| / _` |/ __|| '_ \ | | / _ \ | || __| |  __|  | '__| / _` || '_ ` _ \  / _ \ \ /\ / / / _ \ | '__|| |/ /     
| |  | ||  __/| |_ | (_| |\__ \| |_) || || (_) || || |_  | |     | |   | (_| || | | | | ||  __/ \ V  V / | (_) || |   |   <      
|_|  |_| \___| \__| \__,_||___/| .__/ |_| \___/ |_| \__| |_|     |_|    \__,_||_| |_| |_| \___|  \_/\_/   \___/ |_|   |_|\_\     
                               | |                                                                                               
                               |_|                                                                                               
                                                                                                       Created by IllmaticJV     
                                                                                                                                 
Enter the LHOST for the payload: 
Enter the LPORT for the payload: 
Enter the architecture (32 or 64):4
Enter the output file format (exe, csharp, ps1, etc.): 
Do you want a staged payload? (y/n):
Do you want to migrate the process after the payload is executed? (y/n): 
Enter the output path for the shellcode (press enter to use current folder): 
[+] Payload generated successfully:
./shellcode
Handler created. To access the handler, run screen -r msf_handler
