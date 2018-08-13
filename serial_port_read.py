import serial
import time
import sys
def receive(serial):
    while True:
        data = serial.read_all()
        time.sleep(0.2)
        if data == '':
            continue
        else:
            break
    return data


def write_data():
    ser = serial.Serial('COM4', 9600, timeout=0.2)
    if ser.isOpen():
        print('open success')
    else:
        print('open faild')

    flag = 0
    while flag < 200:
        flag = flag + 1
        data = receive(ser)
        if data != 'EOF':
            print('receive: ', data)
            with open('gps.txt', 'a', encoding='utf-8') as f:
                # ser.write(data)
                f.write(data.decode('utf-8'))
if __name__ == '__main__':
    write_data()
