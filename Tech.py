class Employee:
    def __init__(self, name, role, hours_worked, task_completed):
        self.name = name
        self.role = role
        self.hours_worked = hours_worked
        self.task_completed = task_completed
    
    def work(self):
        pass
    
    def evaluate_performance(self):
        productivity = self.task_completed / max(self.hours_worked, 1)
        
        if productivity > 1.5:
            return "High Performance"
        elif productivity > 0.8:
            return "Medium Performance"
        else:
            return "Low Performance"

class SoftwareEngineer(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Software Engineer", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} (Software Engineer) is coding.")

class DataScientist(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Data Scientist", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} (Data Scientist) is analyzing data.")

class ProductManager(Employee):
    def __init__(self, name, hours_worked, task_completed):
        super().__init__(name, "Product Manager", hours_worked, task_completed)
    
    def work(self):
        print(f"{self.name} (Product Manager) is managing the product roadmap.")

# Simulasi karyawan
employees = [
    SoftwareEngineer("Alice", 40, 70),
    DataScientist("Bob", 35, 30),
    ProductManager("Charlie", 38, 32),
    SoftwareEngineer("David", 45, 20)
]

# Menjalankan simulasi
for employee in employees:
    employee.work()
    print(f"Performance Rating: {employee.evaluate_performance()}\n")
