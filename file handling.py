

"""textfile=open("text.txt",'w')
textfile.write("Hello people")
textfile.close()"""

"""textfile=open("text.txt",'a')
textfile.write("  How are you?")
textfile.write("\n All good?")
textfile.write("\nWhat are you doing now?")
textfile.close()"""

"""textfile=open("text.txt",'r')
print(textfile.read())
textfile.close()"""

"""textfile=open("text.txt",'r')
print(textfile.readline())
textfile.close()"""

textfile=open("text.txt",'r')
print(textfile.readlines(-1))
textfile.close()



