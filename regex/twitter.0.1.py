# some filter to remove the user from a URL
# replace

url = input("URL: ").strip()

username = url.replace("https://twitter.com/,"")

print(f"Username: {username}")

