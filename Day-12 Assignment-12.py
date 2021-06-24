

# Opening a File
# read and write the file
file1=open("myfile.txt","r+")
print(file1.read())
file1.writelines("\n""Hi")
file1.close()

# Closing a File
file1=open("myfile.txt","a")
file1.close()



#Writing a File
file1=open("myfile.txt","w")
L=["This is Harsha \n","CSE \n"]
file1.write("Bharath university \n")
file1.writelines(L)
file1.close()
file1=open("myfile.txt", "r+")
print("Output of the file when read and write")
print (file1.read())
print



# seek(n) takes the file handle to the nth
file1.seek(10)
print("The Output of file when readlines")
print(file1.readline(10))
print(file1.close())




#Appending-will add the element at last
file1=open("myfile.txt","a")
L=["Today \n"]
file1.writelines(L)
print("The Output of the File After Appending")

file1=open("myfile.txt","r")
print(file1.read())
file1.close()




#Task :
file2=open("30 days 30 hour operations.txt","w")
file2.write("I have completed 10 days successfully \n")
print("The Output Of The Task :")
file2=open("30 days 30 hour operations.txt","a")
file2.write("B HARSHA VARDHAN REDDY")
file2=open("30 days 30 hour operations.txt","r")
print(file2.read())
file2.close()





