
from schedule import comps, get_nums_groups, get_nums_pars
import math
from openpyxl import load_workbook

dataset = load_workbook(filename='datasett.xlsx')
sheet = dataset.active

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+max(i, m):(i+1)*k+max(i+1, m)] for i in range(n))

times = {

    1: '08:00-09:30',
    2: '09:50-11:20',
    3: '11:40-13:10',
    4: '13:40-15:10',
    5: '15:30-17:00',
    6: '17:20-18:50',
    7: '19:05-20:35',
    8: '20:50-22:20'
}

time_to_time = {

    '08:00-09:30': [480, 560],
    '09:50-11:20': [590, 680],
    '11:40-13:10': [700, 790],
    '13:40-15:10': [820, 910],
    '15:30-17:00': [930, 1020],
    '17:20-18:50': [1040, 1130],
    '19:05-20:35': [1145, 1235],
    '20:50-22:20': [1250, 1340]
}

max_gr = 14
cp = list(split(range(1, max_gr), 6))



row = 1

for comp in comps:

    for day in comps[comp]:

        for time in comps[comp][day]:

            row += 1
            num = get_nums_groups(comp, day, time)


            start = time_to_time[time][0]
            end = time_to_time[time][1]

            #print(day + ":"  + str(time_to_time[time][0]) + ":" + str(time_to_time[time][1])  + " - ", get_nums_groups(comp, day, time))
    

            sheet[row][0].value = num
            sheet[row][2].value = comp
            sheet[row][1].value = end

            #заполнение для end

            if num > 0:

                if num in cp[0]:
                    sheet[row][3].value = 2
                elif num in cp[1]:
                    sheet[row][3].value = 3
                elif num in cp[2]:
                    sheet[row][3].value = 4
                elif num in cp[3]:
                    sheet[row][3].value = 5
                elif num in cp[4]:
                    sheet[row][3].value = 6
                elif num in cp[5]:
                    sheet[row][3].value = 6


                elif num > 14:

                    if time == times[2] or time == times[3]:

                        sheet[row][3].value = 6

                    elif time == times[5] or time == times[6]:

                        sheet[row][3].value = 4

                    else:

                        sheet[row][3].value = 5



                else:

                    sheet[row][3].value = 0


            if (time == times[2] or time == times[3]) and sheet[row][3].value != 5:

                sheet[row][3].value += 2

            elif (time == times[5] and sheet[row][3].value -3 != 0):

                sheet[row][3].value -= 3

            elif (time == times[2] and sheet[row][3].value -2 != 0):

                sheet[row][3].value -= 2




            if sheet[row][3].value <= 0:
                sheet[row][3].value = 1
            elif sheet[row][3].value > 6:
                sheet[row][3].value = 6

            if (time == times[7] or time == times[8]):
                sheet[row][3].value = 0
            #заполнение для end - 9

            row += 1

            sheet[row][0].value = num
            sheet[row][2].value = comp
            sheet[row][1].value = end - 9
            sheet[row][3].value = sheet[row - 1][3].value - 2

            if sheet[row][3].value <= 0:

                sheet[row][3].value = 1



            #заполнение для start

            row += 1

            sheet[row][0].value = num
            sheet[row][2].value = comp
            sheet[row][1].value = start
            sheet[row][3].value = sheet[row - 1][3].value - 1

            if sheet[row][3].value <= 0:

                sheet[row][3].value = 1

            #заполнение для start + 9

            row += 1

            sheet[row][0].value = num
            sheet[row][2].value = comp
            sheet[row][1].value = start+9
            sheet[row][3].value = sheet[row - 1][3].value - 2

            if sheet[row][3].value <= 0:

                sheet[row][3].value = 1






dataset.save('datasett.xlsx')