print()
print("*** Looping Demo #2 ***")
print()

for item in range(0,5):
    print(item)

    keep_going = input("press <enter> to keep looping, or any key to quit")

    if keep_going != "":
        break

print()
print("We are done")
print()