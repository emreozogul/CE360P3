import serial
import time

bluetooth_port = '/dev/tty.ESP32-BT-EE'

# Establish Bluetooth serial connection
try:
    bluetooth = serial.Serial(bluetooth_port, 115200)
    print("Bluetooth connection established.")
except serial.SerialException:
    print("Failed to establish Bluetooth connection. Check if the port is correct.")
    exit()

def send_credentials():
    ssid = input("Enter WiFi SSID: ")
    password = input("Enter WiFi Password: ")

    # Send credentials over Bluetooth
    bluetooth.write(ssid.encode() + b'\n')
    time.sleep(0.5)  # Delay to ensure data is sent sequentially
    bluetooth.write(password.encode() + b'\n')

    print("Credentials sent successfully.")

try:
    while True:
        option = input("Enter 's' to send WiFi credentials or 'q' to quit: ")

        if option.lower() == 's':
            send_credentials()
        elif option.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please enter 's' or 'q'.")
except KeyboardInterrupt:
    print("\nKeyboard Interrupt. Exiting...")
finally:
    bluetooth.close()
