

class Employee:
    first_name = ""
    last_name = ""
    id = 0
    hourly_pay = 0.0
    
    def __init__(self, first: str, last: str, eid: int, hpay: float):
        """Constructor

        Args:
            first (str):
            last (str]):
            eid (id):
            hpay (float): hourly pay
        """
        self.first_name = first
        self.last_name = last
        self.id = eid
        self.hourly_pay = hpay
        
    def pay(self, hours):
        """Calculate the total payment

        Args:
            hours (float): Hours worked

        Returns:
            float: Total payment
        """
        if hours <= 40:
            return hours * self.hourly_pay
        else:
            extra_pay = (hours - 40) * self.hourly_pay * 1.5
            total = 40 * self.hourly_pay + extra_pay
            return total

def program():
    id = input("Please enter the Employee's ID: ")
    id = int(id)
    
    first = input("Please enter the Employee's First Name: ")
    last = input("Please enter the Employee's Last Name: ")
    hpay = input("Please enter the Employee's Hourly Pay Rate: ")
    hpay = float(hpay)
    hours_worked = input("How many hours did John work this week? ")
    hours_worked = float(hours_worked)
    
    emp = Employee(first, last, id, hpay)
    
    paycheck = emp.pay(hours_worked)
    
    print(emp.first_name + " " + emp.last_name + "'s  paycheck amount is $" + str(paycheck))

if __name__ == "__main__":
    program()