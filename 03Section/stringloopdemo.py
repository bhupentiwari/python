myString = "Madam"

print(myString[0])
print(  myString[len(myString)-1])

# for char in myString:
#     print(char)


for x in range(10,100) :
  #  print(x)
    x =x+10

blog_posts = {"paython" : ["Python string length | len() function to find string length","Python string length | len() function to find string length","test"] , \
              "javascript" : ["JavaScript Display Possibilities","JavaScript has 8 Datatypes"]} 

for category in blog_posts:
    print("print about:",category)
    for p in blog_posts[category] :
        print(p)
    print("-----------------------------")

