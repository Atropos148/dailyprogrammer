# talkingClock - Takes time in HH:MM format, and returns in "hour, minutes" format
# made by Atropos148
import re

hourDict = {
    '00': 'twelve',
    '01': 'one',
    '02': 'two',
    '03': 'three',
    '04': 'four',
    '05': 'five',
    '06': 'six',
    '07': 'seven',
    '08': 'eight',
    '09': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'one',
    '14': 'two',
    '15': 'three',
    '16': 'four',
    '17': 'five',
    '18': 'six',
    '19': 'seven',
    '20': 'eight',
    '21': 'nine',
    '22': 'ten',
    '23': 'eleven',
}

minutesDict = {
    '0': 'oh',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty'
}

time = input('What time is it? (like this -> 02:34)\n')
match = re.match(r'\d\d:\d\d', time)
if match:
    hour = time[:2]
    minute = time[3:]
    sun = 'AM'
    if hour > '11':
        sun = 'PM'
    print(hour)
    print(minute)
    if minute == '00':
        print("It's", hourDict[hour] + ' ' + sun)
    else:
        minuteTest = int(minute) - int(minute[1])
        print(minuteTest)
        minute = minutesDict[str(minuteTest)] + ' ' + minutesDict[minute[1]]
        print("It's", hourDict[hour] + ' ' + minute + ' ' + sun)
