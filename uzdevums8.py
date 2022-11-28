inputLaiks = float(input("Ieavadi laiku:"))
if (inputLaiks >= 6 and inputLaiks <= 11):
    print("Labrīt!")
elif (inputLaiks >= 12 and inputLaiks <= 16):
    print("Labdien!")
elif (inputLaiks >=17 and inputLaiks <= 22):
    print("Labvakar!")
elif (inputLaiks == 23 or inputLaiks <= 5):
    print("Laiks gulēt!")
elif (inputLaiks >= 24):
    print("Nepareizu laiku tu ievadīji draudziņ")