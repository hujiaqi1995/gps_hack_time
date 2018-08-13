import deal_gps_data
def make_date_file(date,time):
    with open('change_time.bat','w') as f:
        f.write('date '+str(date))
        f.write('\ntime '+str(time))


def get_time():
    time, date = deal_gps_data.deal_data()
    time = time[:len(time) - 3]
    time = time[0:2] + ':' + time[2:4] + ':' + time[4:6]
    date = '20' + date[4:6] + '-' + date[2:4] + '-' + date[0:2]
    return date,time


