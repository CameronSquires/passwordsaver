site = input("Please input the website which this account is stored on.")
password = input("Please input the password for the account on this website.")


with open('passwordsaverlist.txt', 'w') as writer:
    writer.write(f"Website: {site}, password: {password}.")


