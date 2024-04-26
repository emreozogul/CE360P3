import eel
import serial
import serial.tools.list_ports

eel.init('web')  # Folder with web files

def find_esp32_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if any(x in port.description for x in ['ESP32', 'CP210x', 'UART Bridge']):  # Check for multiple possible identifiers
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
            eel.receiveMessage(response)  # Send response back to frontend
    except Exception as e:
        eel.receiveMessage(f"Failed to send data: {str(e)}")

eel.start('index.html', size=(700, 500))
