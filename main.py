import models

member1=models.Member("Sara Taha","33")
member2=models.Member("Hazim Mansoor","36")

post1=models.Post("Good","this is body post1")
post2=models.Post("Very Good","this is body post2")
post3=models.Post("Amazing","this is body post3")

print (member1.name)
print (member1.age)

print (post1.title)
print (post1.body)
