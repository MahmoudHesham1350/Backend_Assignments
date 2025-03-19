with open("input.txt",'r') as file:
    for line in file:
        
        line = line.strip()  # remove any newline character ('\n')
        
        # validate if the operands and operation are correct or not 
        if len(line)!=3 or not line[0].isdigit() or not line[2].isdigit() or not line[1] in '+-/*':
            print("invalid input")

            # clarify if there are any error in the operation and write in the file
            with open("output.txt",'a') as output:
                output.write("this operation is not valid "+'\n')
            
            # continue the other operations
            continue

        """  line[0]   line[1]   line[2]
                |         |         |
            [operand][operation][operand]
        """
        error = False
        operation = line[1]
        match operation:
            case '+':
                ans = int(line[0])+int(line[2])
            case '-':
                ans = int(line[0])-int(line[2])
            case '*':
                ans = int(line[0])*int(line[2])
            case '/':
                # validate that there is no zero division
                if int(line[2]) == 0:
                    error = True
                    with open('output.txt','a') as output:
                        output.write("Invalid,you divide by zero in this operation\n")
        
                if not error:
                    ans = int(line[0])/int(line[2])

             
        if not error:
            with open('output.txt','a') as output:
                output.write(line + "= "+str(ans)+'\n')
            
print("the operations were calculated successfully")
        
    
    
