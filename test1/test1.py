def validate(expression):

    stack = [] 
    for paranthesis in expression: 
        if paranthesis == '(': 
            stack.append(paranthesis) 
        elif paranthesis ==')' and len(stack)!=0:  
                stack.pop()
        elif paranthesis ==')' and len(stack)==0:  
                return("invalid")
    if len(stack) == 0: 
        return("valid")
    else: 
        return("invalid")
   

if __name__ == '__main__':
    input_string = input("Enter string expression to validate:")
    print(f'{input_string} is',validate(input_string))
