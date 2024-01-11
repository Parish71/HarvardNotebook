#n = int(input("What is n? "))
#if n < 0:
#    n = int(input("What is n? "))
#    if n < 0:
#        n = int(input())

# 1° version at this implementation
#while True:
#    n = int(input("What is n? "))
#    if n < 0:
#        continue
#    else:
#        break

# 2° version at this implementation
while True:
    n = int(input("What is n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")