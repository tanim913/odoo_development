
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
from datetime import datetime
from dateutil import relativedelta

class BistaEmployee(models.Model):
    _name = "bista.employee"
    _description = "Bista Employee Details"
    _rec_name = 'name'


    name = fields.Char(string="Employee Name")
    employee_id = fields.Char(string="Employee Id")
    joining_date = fields.Date(string="Joining Date")
    marital_status = fields.Char(string="Marital Status")
    designation = fields.Char(string="Designation")
    salary = fields.Float(string="Salary")
    leave_remaining = fields.Integer(string="Leave Remaining")
    on_leave = fields.Boolean(string= "On Leave", default = True)
    payment_ammount = fields.Float(string= "Payment Ammount")
    mbti = fields.Text(string="Type")
    employee_photos = fields.Image(string="Profile photo", max_width=200,max_height=200)
    
    assigned_task =fields.Char(string="Assigned Task")
    supervisor = fields.Char(string="Supervisor")
    assigned_on = fields.Date(string="Assigned On")
    deadline = fields.Date(string="Deadline")
    worked_days =fields.Date.today()


    def calculate_salary(self):
        date1 = datetime.strptime(str(self.worked_days), '%Y-%m-%d').date()
        date2 = datetime.strptime(str(self.joining_date), '%Y-%m-%d').date()

        delta_time = relativedelta.relativedelta(date1, date2)
        difference = delta_time.months + (delta_time.years * 12)

        if difference >= 6 and difference < 12:
            new_salary = self.payment_ammount+10000
            raise UserError("current salary is :"+str(new_salary))

        elif difference >= 12 :
            new_salary=self.payment_ammount+20000
            raise UserError("current salary is : "+str(new_salary))

        else:
            raise UserError("current salary is : "+str(self.payment_ammount))



    def view_information(self):
        info_message  = "Following assignment information \n"+"Assigned task : "+str(self.assigned_task)+"\nAssigned supervior : "+str(self.supervisor)+"\nAssigned date : "+str(self.assigned_on)+"\nDeadline : "+str(self.deadline)
        raise UserError(info_message)
