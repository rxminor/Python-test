print('Hello World')

file_in = open('C:\\Richard\\RichardMinorTextFiles\\TestFile2.txt', 'r')
file_out = open('C:\\Richard\\RichardMinorTextFiles2\\TestFile2New.txt', 'w')
hold = []
hold2 = []
line1 = ''
asterik = '*'
fullname = ''
streetaddr = ''
cityaddr = ''
staddr = ''
zipaddr = ''
for line in file_in:
    hold = line.split(',')
    # print(hold,end='')
    # print('  ')
    # print(hold[0])
    # print(hold[1])
    # print(hold[2])
    # print(hold[3])
    # print(hold[4])
    fullname = hold[0]
    streetaddr = hold[1]
    cityaddr = hold[2]
    staddr = hold[3]
    zipaddr = hold[4]

    # print('Full name',fullname.lstrip())
    # print('Street address',streetaddr.lstrip())
    # print('city ',cityaddr.lstrip())
    # print('state address',staddr.lstrip())
    # print('zip code',zipaddr.lstrip())

    line1 = fullname.lstrip().__str__() + asterik + streetaddr.lstrip().__str__() + asterik + cityaddr.lstrip().__str__() + asterik + staddr.lstrip().__str__() + asterik + zipaddr.lstrip().__str__()
    print(line1)
    file_out.write(line1)

file_in.close()
file_out.close()