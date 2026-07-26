print("--------------Welcome to the Quiz-------------------")

print("Q1. Who is the father of Computer ?")
print("a. Charles Babbage \t\t b. Alan Turing \t\t c. John Von Neumann \t\t d. Steve Jobs")

option = input("Enter your option: ")
if option == "a" or option == "A":
    print("Correct answer")
    print("Q2. Which city is known as pink city ?")
    print("a. Jaipur \t\t b. Udaipur")
    print("c. Jodhpur \t\t d. Ajmer")
    
    option = input("Enter your option: ")
    if option == "a" or option == "A":
        print("Correct answer")
        print("Q3. Which is the largest continent ?")
        print("a. Asia \t\t b. Africa \t\t c. Europe \t\t d. Antarctica")

        option = input("Enter your option: ")
        if option == "a" or option == "A":
            print("Correct answer")
        else:
            print("Wrong answer.")
            
    else:
        print("Wrong answer")
        
else:
    print("Wrong answer")