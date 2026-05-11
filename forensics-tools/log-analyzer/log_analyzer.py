line_number = 0
failed  = 0
unknown = 0
with open("Your log file", "r") as file:
    for line in file:
        line_number = line_number + 1
        if "failed" in line:
            print(line_number, line)
            failed = failed + 1
        if "unknown" in line:
            print(line_number, line)
            unknown = unknown + 1
print("Total unknown attempts:", unknown)
print("Total failed attempts:", failed)
