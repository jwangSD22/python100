import pandas

data = pandas.read_csv('./weather_data.csv')


print(f'{data}\n\n')

monday = data[data.day == 'Monday']


print(monday.temp*9/5 + 32)

