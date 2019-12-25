string = input("enter a string \n")
length=len(string)
count=0
counter=0
while count<length:
      if string[count]== "a" or string[count]== "e" or  string[count]== "i" or string[count]== "o"  or string[count]== "u" :
       counter= counter+1
      count=count +1
print(" the no of vowels in a string are : ", counter)

    
