from modules.scanner import scan_permissions
from modules.analyzer import analyze

print()

print("Linux File Permissions Lab")

print("1 Scan Directory")

print("2 Analyze")

choice = input("> ")

directory = input(

    "Directory: "

)

files = scan_permissions(

    directory

)

if choice == "1":

    for f in files:

        print(f)

elif choice == "2":

    result = analyze(

        files

    )

    for item in result:

        print(item)