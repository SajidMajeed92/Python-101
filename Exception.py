# try:
#     # code that may cause exception
# except:
#     # code to run when exception occurs
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0.

try:

    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# Python try...finally
# In Python, the finally block is always executed no matter whether there is an exception or not.
# The finally block is optional. And, for each try block, there can be only one finally block.
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

finally:
    print("This is finally block.")

# Example for Exceptional Handling
a = 5
b = 2

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero" , e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print("resource Closed")

# Example
try:
    print('try block')
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )

# Example with function

def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate)
        interest = (amount * year * rate) / 100
        print('The Simple Interest is', interest)
        return interest
    except ValueError:
        print('interest rate is out of range', rate)

print('Case 1')
simple_interest(800, 6, 8)

print('Case 2')
simple_interest(800, 6, 800)