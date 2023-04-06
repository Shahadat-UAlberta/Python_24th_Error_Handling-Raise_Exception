num1 = int(input())

num2 = int(input())

try:
    div = num1 / num2
    print(div)
    # Code - 2
    # Code - 3
except ZeroDivisionError:
    print("Error: Zero Division Exception")
except (EOFError, EnvironmentError) as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    print("No Exception here.")
finally:
    print("Always")

print("Done!")

try:
    pass
except Exception as ex:
    pass
"""
try: 
  // Code block 
except Exception as ex:
  // Block -> 
  
2
"""