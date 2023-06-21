import sys
import basic   
def runner():         
    text = input('Please entire path to file: ')
    if text.strip() != "":
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if (i + ":") in text:
                text = text.replace(i + ":", "", 1)
        for i in "/\\":
            if i in text:
                text = text.replace(i, "", 1)
        print(text)
        result, error = basic.run('<stdin>', text)
        if error:
            print(error.as_string())
        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
    ans = str(input("Any other files? (Y/N) "))
    if ans.upper() == "Y":
        runner()
    else:
        sys.exit()
runner()