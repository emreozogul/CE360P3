import eel
import serial
import serial.tools.list_ports

eel.init('web')  # Initialize the web folder

def find_esp32_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"Port: {port.device}, Description: {port.description}, HWID: {port.hwid}")
        if 'ESP32BT' in port.device:  # Look for the specific device name
            return port.device
    return None

@eel.expose
def send_credentials(ssid, password):
    port = find_esp32_port()
    if port is None:
        eel.receiveMessage("ESP32 not found. Please pair with ESP32 and try again.")
        return
    try:
        with serial.Serial(port, 115200, timeout=10) as bt_serial:
            bt_serial.write(f"{ssid}\n".encode())
            bt_serial.write(f"{password}\n".encode())
            response = bt_serial.readline().decode().strip()
            if not response:  # Check if response is empty
                response = "No response from ESP32."
            eel.receiveMessage(response)
    except Exception as e:
        eel.receiveMessage(f"Failed to send data: {str(e)}")

eel.start('index.html', size=(700, 500))
