num1 = int(input())

num2 = int(input())

# try:
#    div = num1 / num2
#except ZeroDivisionError as ex:
#   pass

try:
     div = num1 / num2
     print(div)
     # Code -2
     # Code -3
except ZeroDivisionError as zex:
     print("Error: Zero Division Exception")
except (EOFError, EnvironmentError) as ex:
     print(ex)
except Exception as ex:
     print("ex")
else:
     print("No Exception here.")
finally:
     print("Always")

print("Done!")

# print("Hello")
# print(div)

"""
try :
    // Code block
except Exception 
    // Block -> 
"""