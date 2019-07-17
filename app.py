import re
import csv

'''filename_input = input('Enter filename: ')
day_input = input('Enter day(s) (eg. \"Mon\" or \"Mon-Thur\"): ')
hour_input = input('Enter time (hh:mm - 24 hour): ')

with open(filename_input) as file:
    reader = csv.reader(file)'''
day_input = "Wed"
hour_input = "01:30"

weekdays = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6,
}


class Business():

    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.bool = False
        self.days = ""
        self.hours = ""

    def getName(self):
        return self.name

    def getTime(self):
        return self.time

    def getDict(self):
        return self.timeDict


def addDict(self, key, time_open, time_close):
    self.timeDict[key] = time_open, time_close


def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]
# Function to convert the date format


def convert24(str1):
    # Checking for 12:00 AM
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    # remove the AM
    elif str1[-2:] == "AM":
        return str1[:-2]
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:8]


with open('restaurant_hours.csv') as file:
    reader = csv.reader(file)
    open_list = []
    count = 0
    for row in reader:
        print("Loop start")
        row_obj = Business(row[0], row[1])
        split1 = re.split(r'/', row[1])
        objDict = {}
        for s in split1:
            days = re.findall(r'[A-Z][a-z].-[A-Z][a-z]*|[A-Z][a-z]*', s)
            hours = re.findall(
                r'\d{1,3}:\d{1,3}\s[a-z]{2}|\d{1,3}\s[a-z]{2}', s)
            print(days)
            #print(hours)
            op = hours[0]
            cl = hours[1]
            for d in days:
                print(len(d))
                if len(d) == 3:
                    day_val = weekdays[d]
                    #print(day_val)
                    objDict.update({day_val: [op, cl]})
                if len(d) > 3:
                    start = weekdays[d[0:3]]
                    end = weekdays[d[4:7]]
                    #print(start)
                    #print(end)
                    for i in range(start, end+1):
                        objDict.update({i: [op, cl]})
        print(objDict)

        count += 1
        if count > 3:
            break

test = Business("Osakaya Restaurant",
                "Mon-Thu, Sun 11:30 am - 9 pm  / Fri-Sat 11:30 am - 9:30 pm")

#print(test.getName())
#print(test.getTime())

#day_input = "Wed"
#hour_input = "01:30"
