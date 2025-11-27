"""

Write a “pager” program. Your solution should prompt for a filename, and display the text file 25 lines at a time, pausing
each time to ask the user to enter the word “continue”, in order to show the next 25 lines or enter the word “stop” to
close the file.

"""

filename = input("Enter filename: ")


f = open(filename+".txt", "r")
lines = f.readlines()
f.close()

index = 0
total = len(lines)

while index < total:
    # Show 25 lines
    for i in range(index, min(index + 25, total)):
        print(lines[i], end="")

    index += 25

    if index >= total:
        print("\n--- End of File ---")
        break

    choice = input("\nType c for'continue' to show next 25 lines or s for 'stop' to exit: ").strip().lower()

    if choice == "s":
        print("File closed.")
        break

    if choice != "c":
        print("Invalid input, exiting.")
        break


            
         