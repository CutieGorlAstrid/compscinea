from webbrowser import open
print("Win or fail?")
prompt = input("> ")
if prompt == "win":
    open('win.jpg')
elif prompt == "fail":
    open('fail.jpg')
while True:
    print("\n")
