file = open("users.csv","a")
name = input("Enter your name: ")
age = input("Enter your age: ")
passwd = input("Enter a password to use: ")
username = name[:3] + age
print("Username: " + username)
file.write(username + "," + passwd + "\n")
file.close()
x = input("Press Enter to quit.")
