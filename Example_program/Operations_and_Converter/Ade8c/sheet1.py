# This program code is for matrix representation of e8c */
#                                                       */
# Input:Yalg.txt  Lie bracket calculation result        */
#        Relement.txt R2 elements symbole of [R1,R2]    */
# Output:data.mac matrix for Theorem 11.7.              */
import os
rdir = '/mnt/UandW'
if os.name == 'Windows':
    rdir = 'F:'
homedir= rdir + '/LieG/E8/Digitalization/'
# Function define
def READ_YalgText(sheet):
    cnsFILENAME = open(homedir+'Temp/Yalg.txt', mode='r', encoding="utf-8")
    lines = cnsFILENAME.read()
    for count, line in enumerate(lines.split(';')):
        if count == 6:
            continue
        else:
            line = line.replace('\n', '')
            sheet.append(line)
    cnsFILENAME.close()

def seiretu(sheet1,sheet2):
    for str1 in sheet2:
        if str1 == '':
            break
        str4 = str1.replace('(-', '-(')
        str2 = str4.replace('-', '+-')
        infile = open(homedir+'Relement.txt', mode='r', encoding="utf-8")
        lineRcha = infile.read()
        line = []
        for count1, str3 in enumerate(lineRcha.split('\n')):
            shcl = ''
            for count2, arr in enumerate(str2.split('+')):
                if (str3 in arr):
                    if len(shcl) > 0:
                        shcl = '+' + shcl
                    arr = arr.replace(str3, 'f')
                    arr = arr.replace('11', '1')
                    arr = arr.replace('12', '2')
                    arr = arr.replace('13', '3')
                    arr = arr.replace('D1', 'D')
                    shcl = arr + shcl
                    shcl = shcl.replace('+-', '-')
                    shcl = shcl.replace(';', '')
                    shcl = shcl.replace('\n', '')
            line.append(shcl)
        sheet1.append(line)
    
def chikan1(sheet):
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            str1 = sheet[l][c]
            if str1 != '':
                if (str1[-1] == ')') and ('-((' in str1):
                    sheet[l][c] = sheet[l][c][0:-1]
                    sheet[l][c] = sheet[l][c].replace('-((', '-(')
            c += 1
        l += 1
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            str1 = sheet[l][c]
            Start = str1.find('(')
            if Start > -1:
                su = str1[Start+1:Start+2]
                if su.isdecimal():
                    if (int(su) > 1) and (int(su) < 10):
                        sheet[l][c] = sheet[l][c].replace('('+su+'*', su+'*(')
            Start = str1.find('f*')
            if Start > -1:
                su = str1[Start+2:Start+3]
                su2 = str1[Start+2:Start+4]
                if (su == 'w') or (su == 'x') or (su == 'y') or (su == 'z'):
                    sheet[l][c] = sheet[l][c].replace('f*'+su2, su2+'*f')
            c += 1
        l += 1
    sheet[0][0] = sheet[0][0].replace('DDD', 'D')
    sheet[0][0] = sheet[0][0].replace(',f', '')

def chikan2(sheet):
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            str1 = sheet[l][c]
            Start = str1.find('JD(f')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('JD(f,', 'MDr(')
            str1 = sheet[l][c]
            Start = str1.find('JD(')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('JD(', 'MDl(')
                sheet[l][c] = sheet[l][c].replace(',f)', ')')
            str1 = sheet[l][c]
            Start = str1.find('V(MD')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('V(MD', 'Mv.MD')
                sheet[l][c] = sheet[l][c].replace('))', ')')
            str1 = sheet[l][c]
            Start = str1.find('V(Mv')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('V(Mv', 'Mv.Mv')
                sheet[l][c] = sheet[l][c].replace('))', ')')
            c += 1
        l += 1
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            sheet[l][c] = sheet[l][c].replace('J(D,f)', 'MJl(D)')
            sheet[l][c] = sheet[l][c].replace('J(V(D),f)', 'MJl(Mv.D)')
            sheet[l][c] = sheet[l][c].replace('J(V(V(D)),f)', 'MJl(Mv.Mv.D)')
            c += 1
        l += 1
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            sheet[l][c] = sheet[l][c].replace('J(f,', 'MJr(')
            str1 = sheet[l][c]
            Start = str1.find('V(f)')
            if Start > -1:
                sheet[l][c] = sheet[l][c] + '.Mv'
                sheet[l][c] = sheet[l][c].replace('V(f)', 'f')
            sheet[l][c] = sheet[l][c].replace('J(f,', 'MJr(')
            str1 = sheet[l][c]
            Start = str1.find('V(f)')
            if Start > -1:
                sheet[l][c] = sheet[l][c] + '.Mv'
                sheet[l][c] = sheet[l][c].replace('V(f)', 'f')
            sheet[l][c]=sheet[l][c].replace('J(f,', 'MJr(')
            str1 = sheet[l][c]
            Start = str1.find('V(f)')
            if Start > -1:
                sheet[l][c] = sheet[l][c] + '.Mv'
                sheet[l][c] = sheet[l][c].replace('V(f)', 'f')
            c += 1
        l += 1
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            str1 = sheet[l][c]
            Start = str1.find('I(f')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('I(f,', 'MIr(')
            str1 = sheet[l][c]
            Start = str1.find('I(')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('I(', 'MIl(')
                sheet[l][c] = sheet[l][c].replace(',f)', ')')
            c += 1
        l += 1
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            str1 = sheet[l][c]
            Start = str1.find('C(f')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('C(f,', 'C(')
            str1 = sheet[l][c]
            Start = str1.find('C(')
            if Start > -1:
                sheet[l][c] = sheet[l][c].replace('C(', 'MC(')
                sheet[l][c] = sheet[l][c].replace(',f)', ')')
            c += 1
        l += 1
    L = [[1, 6, 12, 18, 25, 31, 39, 45], [4, 9, 15, 21, 28, 34, 42, 48]]
    C = [[4, 9, 15, 21, 28, 34, 42, 48], [6, 12, 18, 25, 31, 39, 45, 53]]
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            l = L[0][i]
            while l < L[1][i]:
                c = C[0][j]
                while c < C[1][j]:
                    str1 = sheet[l][c]
                    Start = str1.find('*f')
                    if Start > -1:
                        if not('(' in sheet[l][c]):
                            if ('-' in sheet[l][c]):
                                sheet[l][c] = sheet[l][c].replace('-', '-Mt(')
                                sheet[l][c] = sheet[l][c].replace('*f', ')')
                            else:
                                sheet[l][c] = 'Mt(' + sheet[l][c]
                                sheet[l][c] = sheet[l][c].replace('*f', ')')
                        else:
                            sheet[l][c] = sheet[l][c].replace('(', 'Mt(')
                            sheet[l][c] = sheet[l][c].replace('*f', '')
                    c += 1
                l += 1
            j += 1
        i += 1

def chikan3(sheet):
    L = [1, 6, 12, 18, 25, 31, 39, 45]
    i = 0
    while i < 8:
        l = L[i]
        while l < L[i]+3:
            j = 0
            while j < 8:
                c = L[j]
                while c < L[j]+3:
                    sheet[l][c] = sheet[l][c].replace('f', 'ME8')
                    c += 1
                j += 1
            l += 1
        i += 1
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            sheet[l][c] = sheet[l][c].replace('f*', '')
            sheet[l][c] = sheet[l][c].replace('*f', '')
            c += 1
        l += 1

def chikan4(sheet):
    L = [28, 8, 8, 8, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1,
          1, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1, 1,
          1, 1, 1, 8, 8, 8, 1, 1, 1, 8, 8, 8, 1, 1, 1, 1, 1]
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            str1 = sheet[l][c]
            if not('MM[' in str1):
                if str1 != '':
                    sheet[l][c] = '+(' + sheet[l][c] + ')'
                sheet[l][c] = 'MM[' + str(l + 1) + ',' + str(c + 1) + '] : M0[' + str(L[l]) + ',' + str(L[c]) + ']' + sheet[l][c]
                sheet[l][c] = sheet[l][c].replace('M0', 'expand(M0')
                sheet[l][c] = sheet[l][c] + ')'
            c += 1
        l += 1

def makeText(sheet):
    datFile = open(homedir+'Temp/data.mac', mode='w', encoding="utf-8")
    l = 0
    while l < 53:
        c = 0
        while c < 53:
            line = sheet[l][c] + ';\n'
            datFile.write(line)
            c += 1
        l += 1
    datFile.close()


# Main routine
sheet2 = []
READ_YalgText(sheet2)

sheet1 = []
seiretu(sheet1, sheet2)

chikan1(sheet1)

chikan2(sheet1)

chikan3(sheet1)

chikan4(sheet1)

makeText(sheet1)

print('data.mac is created.')