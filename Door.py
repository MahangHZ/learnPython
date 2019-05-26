class Door:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Door.empCount += 1

    def displayCount(self):
        print(
        "Total Employee %d" % Door.empCount)

    def displayEmployee(self):
        print(
        "Name : ", self.name, ", Salary: ", self.salary)