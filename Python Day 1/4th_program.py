token = 15
brand = "mango"

if token == 10:
    print("chips")

elif token == 20:
    if brand == "mango":
        print("mazza")
    elif brand == "sprite":
        print("sprite")
    else:
        print("invalid brand")

else:
    print("invalid token")