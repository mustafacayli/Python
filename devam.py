# # # # class Mustafa:
# # # #     pass

# # # # # constructor
# # # # # calistirilmasi lazim
    
# # # #     def __init__(self,name,year):
# # # #         self.name=name
# # # #         self.year=year
# # # #         print("metod çalıştı")

# # # # #methods
# # # #     def intro(self):
# # # #         print('Hi')

# # # #     def calculateYear(self):
# # # #         return 2022-self.year


# # # # # object

# # # # m1=Mustafa('mustafa',1992)


# # # # print(f'name: {m1.name} age: {m1.calculateYear()}')
 

# # # # m1.intro()

# # # # *****************************************************

# # # class Square:
# # #     pi=3.14

# # #     def __init__(self,edge):
# # #         self.edge=edge

# # #     def alan_hesaplama(self):
# # #         return self.edge*self.edge



# # # s1=Square(13)

# # # print(f'alan: {s1.alan_hesaplama()}')

# # # # ********************************************************************

# # #kalıtım-inheritance

# # class Person():
# #     def __init__(self,fname,lname):
# #         self.fname=fname
# #         self.lname=lname
# #         print('person created')

# #     def who_am_ı(self):
# #         print('ı am a preson')

# # class Student(Person):
# #     def __init__(self,fname,lname,number):
# #         Person.__init__(self,fname,lname)
# #         self.studentNumber=number
# #         print('student created')

# #     #override
# #     def who_am_ı(self):
# #         print('ı am a student')

    
# # class Teacher(Person):
# #     def __init__(self,fname,lname,branch):
# #         super().__init__(fname,lname)
# #         self.branch=branch
# # p1=Person('mustafa','cayli')
# # s1=Student('mahmut','miclevit',123)
# # t1=Teacher('Ali','Yigit','Engineer')

# # print(f'person fname: {p1.fname} lname: {p1.lname}')
# # print(f'student fname: {s1.fname} lname: {s1.lname} student number: {s1.studentNumber}')
# # print(f'teacher fname: {t1.fname} lname: {t1.lname} teachers branch:{t1.branch}')

# # s1.who_am_ı()

# # *************************************************************************

# class Movie():
#     def __init__(self,tittle,director,duration):
#         self.tittle=tittle
#         self.director=director
#         self.duration=duration
#         print('movie objects created')

#     def __str__(self):
#         return f"{self.tittle} by {self.director}"

#     def __len__(self):
#         return self.duration

#     # def __del__(self):
#     #     print('movie object deleted')
#     # silmek için kullanılıyor
# m=Movie('movie name','director name','movie time')

# print(str(m))
# print(len(m))




