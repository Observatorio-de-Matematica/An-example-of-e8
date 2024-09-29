# This program code is for matrix representation of e8c */
#                                                       */
# Input:Cmat.txt  Maxima's matrix definition            */
# Output: Cmat.csv                                      */

import os
rdir = '/mnt/UandW'
if os.name == 'Windows':
    rdir = 'F:'
homedir = rdir + '/LieG/E8/Digitalization/Temp'
filename ='Cmat'
import csv
sheet = ''
sheetc = [[' ']*248 for i in range(248)]
cnsFILENAME = open(homedir+filename+'.txt', mode='r', encoding="utf-8")
lines = cnsFILENAME.read()
for count, line in enumerate(lines.split(';')):
    line = line.replace('\n', '')
    line = line.replace('matrix([', '')
    line = line.replace('])', '')
    line = line.replace('],[', ',')
    sheet = sheet + line
cnsFILENAME.close()

for count, line in enumerate(sheet.split(',')):
    i = int(count / 248)
    j = count % 248
    sheetc[i][j] = line

f = open(homedir+filename+'.csv', "w", newline="", encoding="utf-16")
writer = csv.writer(f, dialect="excel-tab")
#writer = csv.writer(f)
writer.writerows(sheetc)
f.close()
