import pandas as pd

c_date = '/Date(1605946500000)/'
t = (int(c_date.strip('/Date()')))/1000
# print(t)

time = pd.Timestamp(1605946500, unit='s')
t_con = pd.Timestamp(t, unit='s')
# print(time, t_con)


def timestamp_conversion(tdate):
    c_time = (int(tdate.strip('/Date()'))) / 1000
    c_datetime = pd.Timestamp(c_time, unit='s')
    return (c_datetime)

print(timestamp_conversion('/Date(1605942900000)/'))