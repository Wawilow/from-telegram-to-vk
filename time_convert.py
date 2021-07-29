import time
import datetime


def time_now():
    now = datetime.datetime.now()
    return [*str(now).split(' ')[0].split('-'), *(str(now).split(' ')[1].split('.')[0]).split(':')]


def one_day_plus_time(data, delta=1):
    # в дату можно 1)дататам ноу 2)год, месяц, дата 3)год, месяц, дата, час, минута
    # в дельту можно целое число, количество дней сколько при поюсовать
    try:
        delta = datetime.timedelta(days=delta)
    except:
        if delta == 0:
            delta = False
        else:
            return ('error delta convert')
    try:
        return data + delta
    except:
        if type(data) == type([]):
            try:
                if len(data) == 3:
                    data = datetime.date(data[0], data[1], data[2])
                    if delta == False:
                        return data
                    return data + delta
                elif len(data) == 5:
                    # data = datetime.date(data[0], data[1], data[2], data[3], data[4])
                    # старая код, не рабачий
                    data = datetime.datetime(data[0], data[1], data[2], data[3], data[4], 0, 0)
                    # datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
                    # >> > datetime.from iso format('2011-11-04 00:05:23.283+00:00')
                    if delta == False:
                        return data
                    return data + delta
                elif len(data) == 6:
                    # data = datetime.date(data[0], data[1], data[2], data[3], data[4])
                    # старая код, не рабачий
                    data = [int(i) for i in data]
                    data = datetime.datetime(data[0], data[1], data[2], data[3], data[4], 0, 0)
                    # datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
                    # >> > datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
                    if delta == False:
                        return data
                    return data + delta
            except:
                return ('error list ==> date convert')
        return ('error summ data')


def unixtime_convert(date):  # превращает обычную дата тайм дату в юникс дату
    try:
        unixtime = time.mktime(date.timetuple())
        return unixtime
    except:
        return 'error unitime convert'


def data_time_convert(data, delta=0, delta_hours=0):
    # в дату можно 1)дататам ноу 2)год, месяц, дата
    # 3)год, месяц, дата, час, минута, секунда
    # в дельту можно целое число, количество дней сколько при поюсовать
    try:
        delta = datetime.timedelta(days=delta, hours=delta_hours)
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
                elif len(data) == 6:
                    # data = datetime.date(data[0], data[1], data[2], data[3], data[4])
                    data = [int(i) for i in data]
                    data = datetime.datetime(data[0], data[1], data[2], data[3], data[4], data[5], 0)
                    # datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
                    # >> > datetime.from iso format('2011-11-04 00:05:23.283+00:00')
                    return data + delta
            except:
                return ('error list ==> date convert')
        return ('error summ data')


def for_vk_post_convert(): #превращает нынешнюю дату в дату+1 день в формате unixtime
    return unixtime_convert(one_day_plus_time(datetime.datetime.now()))


if __name__ == '__main__':
    # задаем дату и время сейчас, в функцию прибавления 1 дня(можно задать дельту измения)
    # и полученную дату закидываем в преоброзователь из обычной даты\времени в unitime
    print(unixtime_convert(one_day_plus_time(datetime.datetime.now())))
    print(data_time_convert('ff'))