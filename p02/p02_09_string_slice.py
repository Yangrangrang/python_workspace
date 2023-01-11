'''
str = 20230103Sunny
      1234567
날짜: 날씨
'''


def main():
    str = "20230103Sunny"
    date = str[:8]
    print("date:{}".format(date))

    weather = str[8:]
    print("weater:{}".format(weather))

    print("-"*30)
    '''
        year
        mon
        day
        weather
    '''

    year = str[:4]
    print("year:{}".format(year))
    mon = str[4:6]
    print("mon:{}".format(mon))
    day = str[6:8]
    print("day:{}".format(day))
    weather = str[-5:]  # == str[8:]
    print("weather:{}".format(weather))

main()
