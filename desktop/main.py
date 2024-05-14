import serial
import time

def send_data(data):
    bluetooth_serial.write(data.encode())

def send_credentials():
    global ssid, password
    ssid = input("Enter WiFi SSID: ")
    password = input("Enter WiFi password: ")

    send_data(ssid + ":" + password + "\n")
    time.sleep(2) 

try:
    global is_connected
    print("ESP32 Bluetooth Serial Terminal")
    print("Trying to find port '/dev/tty.ESP32-BT-Taha'...")
    bluetooth_port = '/dev/tty.ESP32-BT-Taha'
    
    try:
        bluetooth_serial = serial.Serial(bluetooth_port, 115200, timeout=1)
        is_connected = True
    except serial.SerialException as e:
        print("Failed to establish Bluetooth connection:", e)
        is_connected = False
        
    time.sleep(2)
    
    while is_connected:
        option = input("Enter 'send' to send WiFi credentials or 'quit' to quit: ")

        if option.lower() == 's':
            send_credentials()
        elif option.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 'send' or 'quit'.")
    if not is_connected:
        print("Bluetooth connection is closed.")
except KeyboardInterrupt:
    bluetooth_serial.close()