import eel
import serial
import serial.tools.list_ports

eel.init('web')  # Pointing to the web directory

def get_ports():
    """ List serial ports likely to be Bluetooth connections for ESP32 """
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port.device)
    esp32_ports = [port.device for port in ports if 'ESP32' in port.device]
    return esp32_ports

@eel.expose
def send_credentials(port, ssid, password):
    """ Send credentials over the specified serial port """
    try:
        with serial.Serial(port, 115200, timeout=10) as ser:
            ser.write((ssid + '\n').encode())
            ser.write((password + '\n').encode())
            return "Credentials sent successfully!"
    except Exception as e:
        return f"Failed to send credentials: {str(e)}"

@eel.expose
def list_ports():
    return get_ports()

eel.start('index.html', size=(500, 500))
