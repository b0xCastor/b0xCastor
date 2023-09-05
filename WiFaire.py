import tkinter as tk
import wifi
import os
import base64

try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()
banner = (Fore.RED + """
 ▄█     █▄   ▄█     ▄████████    ▄████████  ▄█     ▄████████    ▄████████ 
███     ███ ███    ███    ███   ███    ███ ███    ███    ███   ███    ███ 
███     ███ ███▌   ███    █▀    ███    ███ ███▌   ███    ███   ███    █▀  
███     ███ ███▌  ▄███▄▄▄       ███    ███ ███▌  ▄███▄▄▄▄██▀  ▄███▄▄▄     
███     ███ ███▌ ▀▀███▀▀▀     ▀███████████ ███▌ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     
███     ███ ███    ███          ███    ███ ███  ▀███████████   ███    █▄  
███ ▄█▄ ███ ███    ███          ███    ███ ███    ███    ███   ███    ███ 
 ▀███▀███▀  █▀     ███          ███    █▀  █▀     ███    ███   ██████████ 
                                                  ███    ███               go to the stars                                                                     
""" + Fore.LIGHTRED_EX)
print(banner)

def scan_wifi():
    wifi_scan = wifi.Cell.all('wlan0') 
    result_text.delete(1.0, tk.END)  

    for cell in wifi_scan:
        result_text.insert(tk.END, f"SSID: {cell.ssid}\n")
        result_text.insert(tk.END, f"Adresse MAC: {cell.address}\n")
        result_text.insert(tk.END, f"Signal Strength: {cell.signal}\n")
        result_text.insert(tk.END, f"Quality: {cell.quality}\n")
        result_text.insert(tk.END, f"Channel: {cell.channel}\n")
        result_text.insert(tk.END, "------------------------\n")

root = tk.Tk()
root.title("Réseaux Wi-Fi")

scan_button = tk.Button(root, text="Scanner Wi-Fi", command=scan_wifi)
scan_button.pack(pady=10)

result_text = tk.Text(root, height=15, width=40)
result_text.pack()

root.mainloop()
