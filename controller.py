import requests
from termcolor import colored

def send(flag, action):
    url = f"http://localhost:5002/set/{flag}/{action}"
    try:
        response = requests.get(url)
        data = response.json()
        print(colored(f"[+] {data.get('message', 'Done')}", "green" if action == "on" else "yellow"))
    except Exception as e:
        print(colored(f"[-] Error: {e}", "red"))

def menu():
    while True:
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
        print(colored("10", "red") + ". Exit")

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
                print(colored("[*] Exiting...", "red"))
                break
            case _:
                print(colored("[!] Invalid choice. Try again.", "red"))

if __name__ == "__main__":
    menu()




