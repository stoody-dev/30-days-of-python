#string methods
a= "akshay!!"
print(len(a))#len calculates length 
print(a.upper())#strings are immutable in python running this command will generate a new string 
print(a.lower())#string methods generates new string 
print(a.rstrip("!"))
print(a.replace("akshay!!","stoody"))
print(a.split("a"))
Heading= "introduction to python"
print(Heading.capitalize())#turns 1st char to uppercase 
str1="welcome"
print(str1.center(50,"."))
str2="there is always room for gell-o"
countstr=str2.count(" ")
print (countstr)
print(str1.endswith("e"))#The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str3 = "my name is akshay. "
print(str3.find("is"))
print(str3.find("stoody"))
str4 = "To Kill A Mocking Bird"
print(str4.istitle())
str5 = "Python is a Interpreted Language" 
print(str5.swapcase())#The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.




