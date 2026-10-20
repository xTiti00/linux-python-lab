tech = input("What technology are you learning? ").lower()
count = 0
def introduce(name):
    print("My name is " + name + " and I am learning Python.")

while tech != "exit":
    if tech == "python":
        print("We're learning the same!")

    elif tech == "linux":   
        print("Linux is powerful!")

    else:
        print("That language is amazing!")
    
    count += 1

    tech = input("What technology are you learning? (Write exit to stop) ").lower()

print("You entered", count, "technologies.")

name = input("What's ur name? ").lower()

introduce(name)