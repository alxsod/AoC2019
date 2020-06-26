content = open('input.txt','r')
digits = content.read().strip('\n').split('-')
pwrange = [int(digit) for digit in digits]

def first():
    possible_pws = list()
    for i in range(pwrange[0],pwrange[1]):
        ints = [int(digit) for digit in str(i)]
        cntr = 0
        check1 = 0
        check2 = False
        for k in range(0,len(ints) - 1):
            print(k)
            if ints[-k-2] <= ints[-k-1]:
                check1 += 1
            if ints[-k-2] == ints[-k-1]:
                check2 = True
        if((check1 == (len(ints) - 1)) and check2):
            possible_pws.append(i)
    return possible_pws


print("Answer 1: ", len(first()))

def second():
    possible_pws = list()
    for i in range(pwrange[0],pwrange[1]):
        ints = [int(digit) for digit in str(i)]
        cntr = 0
        check1 = 0
        check2 = False
        maxindex = len(ints) - 1

        for k in range(0,len(ints) - 1):
            if ints[-k-2] <= ints[-k-1]:
                check1 += 1

   
    


        if(check1 == maxindex and check2 == True):
           possible_pws.append(i)
    return possible_pws

print("Answer 2: ", len(second()))



