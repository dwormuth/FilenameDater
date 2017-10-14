import re

LastDayofMonth = (0,31,28,31,30,31,30,31,31,30,31,30,31)

def decode_filename(fn):
    """Parse a filename for a string of numbers and translate to a date

    Parameters
    ----------
    fn : string

    Returns
    _______
    s : float
        Number of seconds since epoch began

    TODO:
    ----
    1. Barfs on 4 digit years -- or at least 2020 with current fix
    2. Add functionality to assign Quarters

    """
    s = 0.0
    ds = re.findall(r'\d+', fn)
    if ds != []:
        x = list(ds[0])
        yr = x[0]+x[1]
        if int(yr) == 20:
            return s #This will blow up for the year 2020 TODO
        if int(yr) > 63:
            century = 1900
        else: 
            century = 2000
        yri = century + int(yr)


        if len(x) == 4:
            mo = x[2]+x[3]
            #print('Month is ' + mo +' Year is 20' + yr)
            #print ('Last day of the month is the ' + str(LastDayofMonth[int(mo)]))
            dt = datetime(yri,int(mo),LastDayofMonth[int(mo)])
            #print(dt)
            s = time.mktime(dt.timetuple())
            #print(s)
            #print(datetime.fromtimestamp(s).strftime('%y%m%d'))
        elif len(x) == 6:
            mo = x[2]+x[3]
            da = x[4]+x[5]
            #print('Month is ' + mo +' day is '+da+ ' Year is 20' + yr)
            #print('Last day of the month is the ' + str(LastDayofMonth[int(mo)]))
            dt = datetime(yri,int(mo),int(da))
            #print(dt)
            s = time.mktime(dt.timetuple())
            #print(s)
            #print(datetime.fromtimestamp(s).strftime('%y%m%d'))
        else:
            #print(len(ds[0]))
            #print(len(x))
            pass
    return s
