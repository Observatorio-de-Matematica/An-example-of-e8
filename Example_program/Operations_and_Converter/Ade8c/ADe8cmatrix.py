# This program code is for matrix representation of e8c */
#                                                       */
# Input:mat.txt  Lie bracket calculation result         */
#   element_C.txt   base symboles of a matrix e8C       */
#   element_F.txt  File name symboles that stores the base matrices */
# Output: /DEF_temp/ade8cRxxx.mac 248 base matrices     */
#         /DEF/ade8cMatrix.csv   matrix of all elements */
import os
rdir = '/mnt/UandW'
if os.name == 'Windows':
    rdir = 'F:'
homedir= rdir + '/LieG/E8/Digitalization/'

# Module definition
def READ_TextFile9(sheet):
    cnsFILENAME = open(homedir+'Temp/mat.txt', mode='r', encoding="utf-8")
    lines = cnsFILENAME.read()
    for count, line in enumerate(lines.split(';')):
        line = line.replace('\n', '')
        sheet.append(line)
    cnsFILENAME.close()

def ADe8cmatrix(sheet1, sheet9):
    L = [0, 28, 8, 8, 8, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1,
         1, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1, 1,
         1, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1, 1, 1, 1, 1]
    kl = 0
    l = 0
    while l < 53:
        kl = kl + L[l]
        c = 0
        kc = 0
        while c < 53:
            k = l*53 + c
            kc = kc + L[c]
            sheet9[k] = sheet9[k].replace('matrix', '')
            sheet9[k] = sheet9[k].replace('[', '')
            sheet9[k] = sheet9[k].replace('(', '')
            sheet9[k] = sheet9[k].replace(']', '')
            sheet9[k] = sheet9[k].replace(')', '')
            sheet9[k] = sheet9[k].replace('\n', '')
            line = []
            for count, str1 in enumerate(sheet9[k].split(',')):
                line.append(str1)
            jl = 0
            while jl < L[l+1]:
                jc = 0
                while jc < L[c+1]:
                    jk = jl*L[c+1] + jc
                    str2 = line[jk]
                    sheet1[kl + jl][kc + jc] = str2
                    jc += 1
                jl += 1
            c += 1
        l += 1

def Settei(sheet, sheet3, Rch):
    global adline_new
    global lines_C
    if Rch == 'all':
        return
    cns1FILENAME = open(homedir+'element_C.txt', mode='r', encoding="utf-8")
    linesC = cns1FILENAME.read()
    lines_C = linesC
    cns2FILENAME = open(homedir+'element_F.txt', mode='r', encoding="utf-8")
    lines_F = cns2FILENAME.read()
    for count, line in enumerate(lines_F.split('\n')):
        sheet3.append(line)
    adline0 = []
    l = 0
    while l < 248:
        ad = ",".join(sheet[l])
        adline0.append(ad)
        l += 1
    adline_new = ",".join(adline0)
    cns1FILENAME.close()
    cns2FILENAME.close()

def ADe8ctext(sheet, Rst):
    datFile = open(homedir+'Temp/DEF_temp/ade8cR' + Rst + '.mac', mode='w', encoding="utf-8")
    line = 'R1:zeromatrix(248,248);\n'
    datFile.write(line)
    l = 0
    while l < 248:
        c = 0
        while c < 248:
            if sheet[l][c] != '0':
                line = 'R1[' + str(l+1) + '][' + str(c+1) + ']:' + sheet[l][c] + ';\n'
                datFile.write(line)
            c += 1
        l += 1
    datFile.close()

def ADe8cout(sheet, sheet3, Rch):
    global adline_new
    global lines_C
    if Rch == 'all':
        ADe8ctext(sheet, Rch)
        return
    ematrix = [[' '] * 248 for i in range(248)]
    for count, lch in enumerate(lines_C.split('\n')):
        adline_tr = adline_new
        for ct1, line1 in enumerate(lines_C.split('\n')):
            if line1 != lch:
                adline_tr = adline_tr.replace(line1, '0')
        for ct2, line2 in enumerate(adline_tr.split(",")):
            i = int(ct2 / 248)
            j = ct2 % 248
            ematrix[i][j] = line2
        Rst = sheet3[count]
        ADe8ctext(ematrix, Rst)

def outcsv(sheet):
    import csv
    f = open(homedir+'Temp/ade8cMatrix.csv', "w", newline="", encoding="utf-16")
    writer = csv.writer(f, dialect="excel-tab")
    writer = csv.writer(f)
    writer.writerows(sheet)
    f.close()


# Main routine
# read mat.txt to sheet9
sheet9 = []
READ_TextFile9(sheet9)
# memory reserve
ade8matrix = [[' ']*248 for i in range(248)]
# matrix transform
ADe8cmatrix(ade8matrix, sheet9)
#output a specific element
Rch = 'ele'
sheet3 = []
adline_new = ''
lines_C = ''
Settei(ade8matrix, sheet3, Rch)

ADe8cout(ade8matrix, sheet3, Rch)

outcsv(ade8matrix)

print('Matrix definition ade8cR*.mac is created. ')
