
# Convert milliseconds to minutes:seconds:milliseconds, and add 0s for empty digits
def convert_msecs(msecs):
    time_mins = str(msecs // 60000).zfill(2)
    time_secs = str((msecs % 60000) // 1000).zfill(2)
    time_msecs = str(msecs % 1000).zfill(3)[0]

    time_str = "%s:%s:%s" % (time_mins, time_secs, time_msecs)
    return time_str


# Compare two strings for longest duration
def highest_str_time(str_time_one, str_time_two):
    str_time_onem, str_time_twom = int(str_time_one[:2]), int(str_time_two[:2])
    str_time_ones, str_time_twos = int(str_time_one[3:5]), int(str_time_two[3:5])
    str_time_onems, str_time_twoms = int(str_time_one[6]), int(str_time_two[6])
    if str_time_onem > str_time_twom:
        return str_time_one
    elif str_time_onem == str_time_twom and str_time_ones > str_time_twos:
        return str_time_one
    elif (str_time_onem == str_time_twom and str_time_ones == str_time_twos
          and str_time_onems > str_time_twoms):
        return str_time_one
    else:
        return str_time_two
