username = input("Enter your username: ")
password = input("Enter your password: ")

while username != "chrichri156" or password != "PassWord123":
    print("Either you have made a mistake in your username and/or password, or you do not have access to the admin account.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

print(f"Welcome {username}. You are well logged in to the admin account.")
