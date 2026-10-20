

import operator
def calculator(a , operator , b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"

def main():
    print(" === Pyhton CLI Calculator === ")        

    while True:
        try:
            first=input("Enter the first number  (or q to quit ):")

            if first.strip().lower()=='q'  :
                print("GoodBye !!")
                break

            first=float(first)    


            operator=input('Enter operator (+,-,*,/): ')

            

            second=input("Enter the second number  :")

            second=float(second)
            
            result=calculator(first , operator , second)
            print(f'result : {result}')
        except ValueError:
            print("Invalid Input .please enter valid number")
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except Exception as e:
            print(f"An error occurred: {e}")            

if __name__ == "__main__":
    main()
    