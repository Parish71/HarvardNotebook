email = input("What's your email? ").strip()

username , domain = email.split("@")


if username and "." in domain.endswith("edu"):
    print("valid")

else:
    print("invalid")


