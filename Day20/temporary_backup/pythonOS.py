import os
# print(os.getcwd())  #current working directory
# print(os.listdir())  #list of files in current working directory
# print(os.listdir(r"D:\Python\Day20"))  #specific folder


# files=os.listdir()
# for file in files:
#     if file.endswith(".csv"): #.csv, .txt, .py, .docx, .pptx, .xlsx
#         print(file)
# print("file not found")

folder=(r"D:\Python\Day20")
filename="student.csv"
file_path=os.path.join(folder,filename)
print(file_path)