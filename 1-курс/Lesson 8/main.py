        #   ******файлы******

# myfile = open("hello.txt", "w")
# myfile.close()

# try:
#     comefile = open("Lesson 8/hello.txt", "w")
#     try:
#         comefile.write("hello chi den")
#     except Exception as e:
#         print(e)
#     finally:
#         comefile.close()
# except Exception as ex:
#     print(ex)   

# with open("Lesson 8/hello.txt", "w") as somefile:
#     somefile.write("\ngood bye, world") 

# with open("Lesson 8/hello.txt", "a") as somefile:
#     print("\nhello world", file=somefile)   

# from email import message


# with open("Lesson 8/hello.txt", "r") as file:
#     # for line in file:
#     #     print(line)             
#     # str1 = file.readline()
#     # print(str1, end="")
#     # str2 = file.readline()
#     # print(str2, end="")
#     line = file.readline()
# #   while line:
# #     print(line, end="")
# #     line = file.readline  
#     contents = file.readline()
#     print(contents)

# FILENAME = "Lesson 8/messages.txt"
# messages = []

# while True:
#     message = input("Enter text:")
#     if message == "":
#         break
#     messages.append(message + "\n")
# with open(FILENAME, "a") as file:
#     for msg in messages:
#         file.write(msg)    

# print("Read messages")
# with open(FILENAME, "r") as file:
#     for msg in file:
#         print(msg, end="")

# from asyncore import write
# from fileinput import close


# file = open("my_file.txt," "w")
# file.write("hello aibek")
# file.close()
