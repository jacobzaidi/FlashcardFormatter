'''
Mandarin Flashcard Formatting Application

This application takes Chinese characters
I want to learn, and formats them along
with their pinyin into the correct format
that I can then place into my flashcard app
and learn.

By Jacob Zaidi
'''


import pinyin

file_input = open("chars.txt", "r", encoding="utf-8")
file = file_input.read()
file_contents = ""
for i in file:
    if "，" not in i:
        file_contents += i
        file_contents += "\t"
        file_contents += pinyin.get(i, format="strip")
        file_contents += "\n"

file_output = open("output.txt", "w", encoding="utf-8")
file_output.write(file_contents)
file_output.close()
print("*** Extraction Complete ***")
file_input.close()
