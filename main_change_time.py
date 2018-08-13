import serial_port_read
import deal_gps_data
import generate_time
import time
import os
import  execute_change_time

if __name__ == '__main__':
    os.remove('gps.txt')
    os.remove('change_time.bat')
    serial_port_read.write_data()
    time.sleep(1)
    time,date = generate_time.get_time()
    generate_time.make_date_file(time,date)

    execute_change_time.run()

