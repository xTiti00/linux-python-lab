try:
    age = int(input("Introduce your age here: "))
    if age < 0:
        print("Age cannot be negative")

    else:
        print(f"You are {age} years old")

except ValueError:
    print("You must introduce a number")