import time
import datetime


def one_day_plus_time(data, delta=1):#в дату можно 1)дататам ноу 2)год, месяц, дата 3)год, месяц, дата, час, минута
    #в дельту можно целое число, количество дней сколько при поюсовать
    try:
        delta = datetime.timedelta(days = delta)
    except:
        return ('error delta convert')
    try:
        return data + delta
    except:
        if type(data) == type([]):
            try:
                if len(data) == 3:
                    data = datetime.date(data[0], data[1], data[2])
                    return data + delta
                elif len(data) == 5:
                    data = datetime.date(data[0], data[1], data[2], data[3], data[4])
                    return data + delta
            except:
                return ('error list ==> date convert')
        return ('error summ data')


def unixtime_convert(date): #превращает обычную дата тайм дату в юникс дату
    unixtime = time.mktime(date.timetuple())
    return unixtime


def for_vk_post_convert(): #превращает нынешнюю дату в дату+1 день в формате unixtime
    return unixtime_convert(one_day_plus_time(datetime.datetime.now()))


if __name__ == '__main__':
    print(unixtime_convert(one_day_plus_time(datetime.datetime.now())))