
def deal_data():
    data_time = ''
    line = 0
    with open('gps.txt',encoding='utf-8') as f:

        while line < 2000:
            line = line + 1
            datas = f.readline().split(',')
            if datas[0] == '$GPRMC' and datas[1] != '' and datas[9] != '':
                # print(datas)
                data_time = datas[1]
                data_day = datas[9]
                # print(datas[0],data_time,data_day)
                break
    return data_time,data_day