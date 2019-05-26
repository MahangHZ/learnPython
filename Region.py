from firstProject.cn.mahang.firstProject.Door import Door
from firstProject.cn.mahang.firstProject.Animal import Animal

door = Door("aaa", 2000)
animal = Animal("claw AAA", "tail ttt")
print(animal.get_claw())
print(animal.get_tail())
print(animal.a)

animal2 = Animal("ddd", "fff");
print(animal2.get_claw())
print(animal2.get_tail())
print(animal2.a)

list1 = {}
for i in range(1, 10, 1):
    animal = Animal(str(i), str(i + 1))
    list1[i] = animal
print(list1)
