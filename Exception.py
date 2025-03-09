try:
    result = 10 / 0
except ZeroDivisionError as e:
    
    print(f"Error: {e}")
else:
    print("No exceptions occurred.")
finally:
    print("This will always run, no matter what.")
