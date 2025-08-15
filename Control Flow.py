marks = int(input("Enter the student's marks(0-100):"))
# Grading system based on the marks
if marks > 70:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: Credit")
elif marks >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")

    # Print numbers 0 to 4
for i in range (5):
    print(i)

countdown = 5
while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1
    print("Blast off! 🚀")
    
def greet(name):
    print("Hello, " + name + "! 👋")
#Calling the Function
greet("Alice")
greet("Bob")
 
def check_even_odd(number):
    if number % 2 == 0:
        print(number,"is even! ⚖️")
    else:
        print(number, "is odd! 🎯")
        check_even_odd(10)