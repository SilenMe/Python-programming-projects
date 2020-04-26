import os
def rename_files():
    file_list=os.listdir(r"D:\projects\prank\prank")
    saved_path = os.getcwd()
    print("current working drectory is"+saved_path)
    os.chdir(r"D:\projects\prank\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"12345667890"))
    os.chdir(saved_path)    
rename_files()
