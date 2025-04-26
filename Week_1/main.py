# erase any content in the output.txt
with open('output.txt', 'w') as file:
    pass 



with open("input.txt",'r') as file:
    for line in file:
        
        line = line.strip()  # remove any newline character ('\n')
        parts = line.split(' ',3)   # split(separator, maxsplit)
        

        # if the user enters an empty line
        if len(parts)==1 and parts[0]=='':
            continue
        
        
        # validate if the operands and operation are correct or not 
        if  not len(parts) == 3 or not parts[0].isdigit() or not parts[2].isdigit() or not parts[1] in '+-/*':
            print("invalid input")

            # clarify if there are any error in the operation and write in the file
            with open("output.txt",'a') as output:
                output.write("this operation is not valid "+'\n')
            
            # continue the other operations
            continue

        """  parts[0]   parts[1]   lineparts[2]
                |         |         |
            [operand][operation][operand]
        """
        error = False
        operation = parts[1]
        match operation:
            case '+':
                ans = int(parts[0])+int(parts[2])
            case '-':
                ans = int(parts[0])-int(parts[2])
            case '*':
                ans = int(parts[0])*int(parts[2])
            case '/':
                # validate that there is no zero division
                if int(parts[2]) == 0:
                    error = True
                    with open('output.txt','a') as output:
                        output.write("Invalid,you divide by zero in this operation\n")
        
                if not error:
                    ans = int(parts[0])/int(parts[2])

             
        if not error:
            with open('output.txt','a') as output:
                output.write(line + "= "+str(ans)+'\n')
            
print("the operations were calculated successfully")
        
    
    
