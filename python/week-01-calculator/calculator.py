print("You can exit by pressing q.")

while True:
    try:
        print("You can exit by pressing q.")

        num1 = input("Introduce the first number: ")

        if num1.lower() == "q":
            break
        
        num1 = int(num1)
        
        op = input("Introduce the operation (+, -, *, /): ")

        if op.lower() == "q":
            break

        num2 = input("Introduce the second number: ")

        if num2.lower() == "q":
            break
        
        num2 = int(num2)

        if op == "+":
            print(f"{num1 } + {num2}")
            print(num1 + num2 )
        
        elif op == "-":
            print(f"{num1 } - {num2}")
            print(num1 - num2)

        elif op == "*":
            print(f"{num1 } * {num2}")
            print(num1 * num2)
        
        elif op == "/":
            if num2 == 0:
                print("You can't divide by zero")

            else:
                print(f"{num1 } / {num2}")
                print(num1 / num2)

        else:
            print("That's not a valid operation.")
            

    except ValueError:
        print("You can't do this operation.")
    

