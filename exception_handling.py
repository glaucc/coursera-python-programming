# try:
#     items = [1,2,3,4,5]
#     item = items[5]
#     print(item)
# except:
#     print("Item does not exit in the list")


# def divide_by(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 0
#     except Exception as e:
#         print("Something went wrong!", e)
#         print(e.__class__)
# ans = divide_by(40, 0)
# print(ans)

try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("The file could not be found")

