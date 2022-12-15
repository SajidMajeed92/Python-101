# f = open("C:/Python38/README.txt")  # specifying full path
# Example
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()

# Another way to write the above example
with open("data.txt", "r") as f:
    content = f.read()
    print(content)



