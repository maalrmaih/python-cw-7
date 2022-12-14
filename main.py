
# # write your code here
# class person:
#     name="msaeid"
#     age=20
#     def is_adult(self):
#         if self.age > 18:
#             print("you have too much responsibiliit")
#         else:
#             print("lucky u")            


# first_person=person()
# print(first_person.is_adult())

# class person:
#     
#     if s

# print(first_person.age)
# print(first_person.name)
# if first_person.age >= 18:

#     print("you have too much responsibiliit")

# else:
#     print("lucky you")

    # name="msaeid"
    # age=20
    # def is_adult(self):
    #     if self.age > 18:
    #         print("you have too much responsibiliit")
    #     else:
    #         print("lucky u") 
class Peason :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age > 18:
            print("you have too much responsibiliit")
        else:
            print("lucky u")    
    def __str__(self):
        return f"my name {self.name}, and my age {self.age}"

first_person = Peason("musad" , 20)
print(first_person)


