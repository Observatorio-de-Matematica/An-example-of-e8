# This program code is for matrix representation of e8c */
#                                                       */
#  Remove blank lines in Maxima's matrix definition.    */
# Input:/DEF_temp/ade8cRxxx.mac 248 base matrices       */
# Output: /DEF_New/ade8cRxxx.mac 248 base matrices      */

import glob
import os
rdir = '/mnt/UandW'
if os.name == 'Windows':
    rdir = 'F:'
homedir= rdir + '/LieG/E8/Digitalization/'
files = glob.glob(homedir + "Temp/DEF_N/*")
for file in files:
    Ofile = open(file, mode='r', encoding='UTF-8')
    nfile = file.replace('DEF_N', 'DEF_New')
    Nfile = open(nfile, mode='w', encoding='UTF-8')
    lines = Ofile.read()
    for count, line in enumerate(lines.split(';')):
        if line != '\n':
            line = line.replace('\n', '')
            line = line.replace('\"', '') + (';\n')
            Nfile.write(line)
    Ofile.close()
    Nfile.close()