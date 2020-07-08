class SalesPerson:
    def __init__(self, salesperson_first_name, salesperson_last_name, salesperson_employee_id, salesperson_salary):
        self.first_name = salesperson_first_name
        self.last_name = salesperson_last_name
        self.employee_id = salesperson_employee_id
        self.salary = salesperson_salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants):
        self.pants_sold.append(pants)

    def display_sales(self):
        for i in self.pants_sold:
            print('color: ',i.color,', waist_size: ',i.waist_size,', length: ',i.length,', price: ',i.price)

    def calculate_sales(self):
        for i in self.pants_sold:
            self.total_sales += i.price
        return self.total_sales
    def calculate_commission(self,percentage):
        return percentage*self.total_sales
        