import logging
try:
    print("try .....")
    #a = int("a")
    r = 10/0
    print("result:", r)
except ZeroDivisionError as e:
    print("except:", e)
    logging.exception(e)
except ValueError as e:
    print('ValueError:', e)
except Exception as e:
    print('Exception:', e)
else:
    print('No Exception:')
finally:
    print("finally")
print("end")