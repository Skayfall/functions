def date_autumn(dates):
    year = 0
    day = 0
    month = 0

    for i in dates:
        if int(i.split('-')[2]) > year and (i.split('-')[0] == '09' or i.split('-')[0] == '10' or i.split('-')[0] == '11'):
            year = int(i.split('-')[2])

    for i in dates:
        if str(year) in i.split('-')[2] and (i.split('-')[0] == '09' or i.split('-')[0] == '10' or i.split('-')[0] == '11'):
            if int(i.split('-')[0]) > month:
                month = int(i.split('-')[0])

    for i in dates:
        if str(year) in i.split('-')[2] and str(month) in i.split('-')[0]:
            if int(i.split('-')[1]) > day:
                day = int(i.split('-')[1])

    for i in dates:
        if str(day) in i.split('-')[1] and str(year) in i.split('-')[2] and str(month) in i.split('-')[0]:
            return i
