import sys
import basic
import keyboard
import os
import time
text = 'RUN("untitled.pycf")'
result, error = basic.run('<stdin>', text)
if error:
    print(error.as_string())
elif result:
    if len(result.elements) == 1:
        print(repr(result.elements[0]))
    else:
        print(repr(result))
print("Press 'q' to exit.")
while True:
    if keyboard.is_pressed('q'):
        break
    time.sleep(0.1)
file = open(text, "r+")
file.truncate(0)
file.close()