num1 = int(input())

num2 = int(input())

# try:
#    div = num1 / num2
#except ZeroDivisionError as ex:
#   pass

try:
     div = num1 / num2
     print(div)
except ZeroDivisionError as zex:
     print("Error: Zero Division Exception")
except Exception as ex:
     print("Error : Division by Zero")

print("Done!")

# print("Hello")
# print(div)

"""
try :
    // Code block
except Exception 
    // Block -> 
"""