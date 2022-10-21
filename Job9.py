left = "/"
right = "\\"
base = "__"

userinput = int(input("hauteur : "))

for i in range(userinput):
    print((userinput -i) * " " + left + ((i * 2) * ' ') + right)
    if i == userinput - 1:
        print (left + base * userinput + right)