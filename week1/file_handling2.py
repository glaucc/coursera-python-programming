try:
    with open("filewrite.txt", "w") as file:
        file.write("Hii!")
except FileNotFoundError as e:
    print("Error:", e)