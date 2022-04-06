try:
    print(f"Here we should test the try block with division by 0 {5/0}")
except ZeroDivisionError:
    print(f"Thanks to try-except code block, division by zero error is skipped and this msg is printed successfully")
