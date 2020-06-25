def first(opcode_arr):
    cntr = 0
    arr_size = len(opcode_arr) - 1
    while True:
        opcode = opcode_arr[cntr % arr_size]
        rel_index_1 = opcode_arr[(cntr + 1) % arr_size]
        rel_index_2 = opcode_arr[(cntr + 2) % arr_size]
        rel_index_3 = opcode_arr[(cntr + 3) % arr_size]
        if opcode == 1:
            res = opcode_arr[rel_index_1] + opcode_arr[rel_index_2] 
            opcode_arr[rel_index_3] = res
        if opcode == 2:
            res = opcode_arr[rel_index_1] * opcode_arr[rel_index_2] 
            opcode_arr[rel_index_3] = res               
        if opcode == 99:
            break
        cntr += 4
opcodes_cs = open('input.txt','r')
opcode_arr = opcodes_cs.read().strip('\n').split(',')
opcode_arr = [int(opcode) for opcode in opcode_arr]  
opcode_arr[1] = 12
opcode_arr[2] = 2                                                       

first(opcode_arr)
print("Answer 1: " + str(opcode_arr[0]))

def second():
    def inner(i,j):
        opcodes_cs = open('input.txt','r')                                                            
        opcode_arr = opcodes_cs.read().strip('\n').split(',')                                         
        opcode_arr = [int(opcode) for opcode in opcode_arr]                                           
        opcode_arr[1] = j                                                                             
        opcode_arr[2] = i                                                                             
        first(opcode_arr)                                                                             
        return opcode_arr                                                                             
                                                                                                      
    for i in range(0,99):
        for j in range(0,99):
            return_arr= inner(i,j)
            if return_arr[0] == 19690720:
                return_str = "Answer 2: " + str(100 * return_arr[1] + return_arr[2] )
                return return_str
       
    for i in range(0,99):                                                                                
         for j in range(0,99):                                                                           
             return_arr = inner(j,i)
             if return_arr[0] == 19690720:
                return_str = "Answer 2: " + str(100 * return_arr[1] + return_arr[2])
                return return_str 

print(second())
