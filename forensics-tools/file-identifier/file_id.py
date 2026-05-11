import os
total = 0
suspicious_files = 0
files = os.listdir("/path/to/directory") 
for filename in files:
    file_type = "." + filename.split(".")[-1].lower()
    type = ""
    if file_type == ".pdf": type = "PDF"
    elif file_type == ".jpg": type = "JPG"
    elif file_type == ".exe": type = "EXE"
    elif file_type == ".dmg": type = "DMG"
    elif file_type == ".zip": type = "ZIP"
    elif file_type == ".png": type = "PNG"
    elif file_type == ".docx": type = "DOCX"
    elif file_type == ".gif": type = "GIF"
    elif file_type == ".heic": type = "HEIC"
    elif file_type == ".pkg": type = "PKG"
    elif file_type == ".app": type = "APP"

    suspicious = False
    if type == "EXE" or type == "DMG" or type == "ZIP" or type == "PKG" or type == "APP": suspicious = True

    print("Filename:", filename)
    print("Extension:", file_type)
    print("File type:", type)
    if suspicious == True:
        print("WARNING: Executable file detected — flag for investigation")
    else:
        print("Status: No immediate threat detected")
    if suspicious == True:
        suspicious_files = suspicious_files + 1
    total = total + 1



print("Total files analyzed:" + str(total))
print("Suspicious files detected:" + str(suspicious_files))
