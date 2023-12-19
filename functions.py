import csv
import datetime

def get_info(my_date: datetime.date) -> str:
        with open ('task4/dataset.csv', 'r', encoding = "utf-8") as f:
            reader = csv.reader(f)
            data = list(reader)
            for row in data:
                if str(row[0][0:10]) == str(my_date):
                    return (row[1]) + ' ' + (row[2]) + ' ' + (row[3]) + ' ' + (row[4]) + ' ' + (row[5]) + ' ' + (row[6])
                if str(my_date) < str(row[0][0:10]):
                    return None
print(get_info(datetime.date(2023,12,7)))

def get_info_XY(my_date: datetime.date) -> str:
    with open('task4/x.csv', 'r', encoding = "utf-8") as x, open('task4/y.csv', 'r', encoding="utf-8") as y:
        reader_x = csv.reader(x)
        data_x = list(reader_x)
        reader_y = csv.reader(y)
        data_y = list(reader_y)
        counter = 0
        for row in data_x:
            if str(row[0][0:10]) == str(my_date):
                return data_y[counter]
            if str(my_date) > str(row[0][0:10]):
                counter+=1 
            if str(my_date) < str(row[0][0:10]):
                    return None
                
print(get_info_XY(datetime.date(2023,12,7)))
         

def get_info_year(my_date: datetime.date) -> str:
    year = my_date.strftime("%Y")
    file_name = 'task4/' + year + '0101_' + year + '1231.csv'
    try:
        with open(file_name, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)
            result = ""
            for row in data:
                result += row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4] + ' ' + row[5] + ' ' + row[6] + '\n'
            return result
    except FileNotFoundError:
        return None
# print(get_info_year(datetime.date(2008,12,7)))

def get_info_week(my_date: datetime.date) -> str:
    my_week = my_date.weekday()
    start_date = my_date - datetime.timedelta(days=my_week)
    print(start_date)
    end_date = my_date + datetime.timedelta(days=6 - my_week) 
    print(end_date)
    
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")
    
    file_name = 'task4/' + start_date_str + '_' + end_date_str + '.csv'
    print(file_name)
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)
            result = ""
            for row in data:
                result += row[1] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4] + ' ' + row[5] + ' ' + row[6] + '\n'
            return result
    except FileNotFoundError:
        return None
    
print(get_info_week(datetime.date(2023, 11, 16)))



