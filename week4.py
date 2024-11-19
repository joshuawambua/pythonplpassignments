# a poem aboutpoem.txt
#  end of worls
#file handling operations
poem_filename = "poem.txt"

try:
    with open(poem_filename, "w") as poem_file:
        poem_file.write("The End\n")
        poem_file.write("The skies grew dark, no sun in sight,\n")
        poem_file.write("A chilling wind carried the night.\n")
        poem_file.write("Earth stood silent, hearts full of dread,\n")
        poem_file.write("As whispers told of days ahead.\n\n")
        poem_file.write("The oceans roared, mountains crumbled,\n")
        poem_file.write("The world in chaos, deeply humbled.\n")
        poem_file.write("Echoes of laughter, now memories faded,\n")
        poem_file.write("Life's final moments, a beauty jaded.\n\n")
        poem_file.write("Yet in the stillness, hope did gleam,\n")
        poem_file.write("A spark within the darkest dream.\n")
        poem_file.write("For every end births something new,\n")
        poem_file.write("The end, it seems, is just the view.\n")
        poem_file.write("By Mdayz Mcherner.\n\n")
    print(f"File '{poem_filename}' created successfully!")
except Exception as e:
    print(f"Error creating the file: {e}")


modified_filename = "modified_poem.txt"

try:
    with open(poem_filename, "r") as poem_file:
        content = poem_file.readlines()

    #appending
    content.append("\n-- A reflection on endings and beginnings --\n")

    with open(modified_filename, "w") as modified_file:
        modified_file.writelines(content)
    print(f"Modified file '{modified_filename}' created successfully!")
except FileNotFoundError:
    print(f"Error: File '{poem_filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# poem.txt
# Error handling
try:
    user_file = input("Enter the filename to read: ")
    with open(user_file, "r") as file:
        print("\nFile Content:\n")
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{user_file}' does not exist.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
