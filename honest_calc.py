msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg = [0,1,2,3,4,5,6,7,8,9,"Are you sure? It is only one digit! (y / n)",
"Don't be silly! It's just one number! Add to the memory? (y / n)", 
"Last chance! Do you really want to embarrass yourself? (y / n)"]
memory = 0

def is_one_digit(v):
    if v in [-10, -9, -8, -7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]:
        return True
    else:
        return False

def check(v1,v2,v3):
    msg=""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3=="*":
        msg += msg_7
    if (v1==0 or v2==0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8
    if msg!="":
        msg = msg_9+msg
        print(msg)

while True:
    print(msg_0)
    calc = input()
    x, oper, y = calc.split()
    
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in ["+", "-", "*", "/"]:
        print(msg_2)
        continue
    check(x,y,oper)
    if oper == "+":
        result = x+y
    if oper == "-":
        result = x-y
    if oper == "*":
        result = x*y
    if oper == "/":
        if y==0:
            print(msg_3)
            continue
        else:
            result = x/y
    print(float(result))
    while True:
        print(msg_4)
        answer_4 = input()
        if answer_4 == "y":
            if is_one_digit(result):
                msg_index=10
                while True:
                    print(msg[msg_index])
                    answer_10=input()
                    if answer_10 == "y":
                        if msg_index < 12:
                            msg_index +=1
                        else: 
                            memory = result
                            break
                    elif answer_10 == "n":
                        break
                    else:
                        continue
            
            else:
                memory = result
                break
        elif answer_4 == "n":
            break
        else:
            continue
        break
    print(msg_5)
    while True:
        answer_5 = input()
        if answer_5 == "y":
            break
        elif answer_5 == "n":
            break
        else:
            continue
    if answer_5 == "y":
        continue     
        
        
    break
    
