"""
EXCEPTION
==========
An error that occurs while a program is running and interrupts
the normal flow of execution

SYNTAX ERROR: occurs when the user breaks the rules of the programing language
the interpreter does not know what to do// problem with the structure of the code

EXCEPTION HANDLING
==================
try:  # tells the interpreter to try out the code
    # code that might cause an exception

except:  # this is used when an exception occurs in the try: and prevents the program from crashing
    # what to do if an exception occurs

try:
    age = int(input("Enter age: "))

except:
    print("Something went wrong!")

print("The program would still run")

It is not always advisable to use except immediately

#Example
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Enter a valid number")

#EXAMPLE
try:
    number1 = int(input("Enter the second number: "))
    number2 = int(input("Enter the second number: "))

    answer = number1/number2
    print("Answer is: ", answer)

except ValueError:
    print('invalid value')

except ZeroDivisionError:
    print("The second number should not be 0")

print("The rest of the program")

#TYPE ERROR
age = "18"
print(age + 5)

# attribute error
movies = ("GOT", "ARROWS")
movies.append("Grimm")

# Index error
movies = ("GOT", "ARROWS")
print(movies[2])

# Except can handle many different types of exceptions at once
try:
    number  = int(input("enter a number: "))
except (ValueError, TypeError):
    print("")

try:
    number  = int(input("enter a number: "))
except ValueError as ex:
    print("This error happened: ", ex)

try:
    number = int(input("enter a number: "))
except ValueError:
    print("")
except Exception as error:
    # fall back
    print("This error happened: ", error)

try:
    number = int(input("-> "))
    # rest of code
except Exception as ex:
    print("")
else:
    # else block executes if no exception occurred

try:
    file_handle = open("students.txt", 'r')
    # codes
except FileNotFoundError:
    print("File does not exist")
except Exception as ex:
    print("An error has occurred while opening the file")
finally:
    # this is called clean-up technique and is not part of the main/rest of the program
    # this operation is related to the previous
    file_handle.close()

age = int(input("Age: "))
if age < 0:
    raise ValueError("invalid input")
    # raising the exception purposefully and cause the program to crash

"""

class InvalidWithdrawAmount(Exception):  # inheritance from exception class
    pass  # everything that belongs to the Exception class belongs to this class

class AcoountSetUpError(Exception):
    pass


class Account:
    def __init__(self, amount, name):
        if amount < 0:
            raise AcoountSetUpError("insufficient amount error")
        self.__balance = amount
        self.__name = name

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InvalidWithdrawAmount("Amount bigger than the balance")
        self.__balance -= amount
        print("withdraw done successfully")
        print("new balance", self.__balance)

try:
    this_account = Account(-10000, "Jules")
except Exception as ex:
    print("Sorry, object was not created because: ", ex)