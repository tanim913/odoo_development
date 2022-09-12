
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning


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


    