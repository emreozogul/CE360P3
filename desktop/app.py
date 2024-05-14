import eel
import serial
import time
eel.init('web')  

bluetooth_port = '/dev/tty.ESP32-BT-Taha'

try:
    bluetooth_serial = serial.Serial(bluetooth_port, 115200, timeout=1)
except serial.SerialException as e:
    print("Failed to establish Bluetooth connection:", e)
    exit()
    
time.sleep(2)

@eel.expose
def send_credentials(ssid, password):
    try:
        while True:
            send_data(ssid + ":" + password + "\n")
            print(ssid, password)
            time.sleep(2) 

    except KeyboardInterrupt:
        bluetooth_serial.close()
    
    
def send_data(data):
    bluetooth_serial.write(data.encode())
    

eel.start('index.html', size=(500, 500))
