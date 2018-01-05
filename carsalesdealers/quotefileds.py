import csv
f_writ = open('latest10_carsales_2017_09_v4.csv', 'wb')
csvReader = csv.reader('latest5_carsales_2017_09_v4.csv')
writer = csv.writer(f_writ, delimiter=';',
                lineterminator='\r\n',
                quotechar = "'"
                )

for row in csvReader:

    writer.writerow([row,'\"text\"'])

f_writ.close()
