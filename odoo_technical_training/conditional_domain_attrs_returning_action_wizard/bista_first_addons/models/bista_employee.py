
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class BistaEmployee(models.Model):
    _name = "bista.employee"
    _description = "Bista Employee Details"
    _rec_name = 'name'

    def _get_default_date(self):
        return fields.Date.today()

    first_name = fields.Char(string="Employee First Name")
    last_name = fields.Char(string="Employee Last Name")
    name = fields.Char(string="Employee Name")
    employee_id = fields.Char(string="Employee Id")
    joining_date = fields.Date(string="Joining Date")
    date_of_birth = fields.Date(string="Date of Birth")
    marital_status = fields.Char(string="Marital Status")
    designation = fields.Selection([('Trainee', 'Trainee'), ('Junior_dev', 'Junior Developer'), ('Senior_dev', 'Senior Developer'), ('Dev', 'Developer'), (
        'ml_engineer', 'Machine Learning Engineer'), ('android_dev', 'Android Developer'), ('pro_manager', 'Project Manager')], string='Designation')
    salary = fields.Float(string="Salary")
    leave_remaining = fields.Integer(string="Leave Remaining")
    experience = fields.Integer(string="Years of Experience")
    on_leave = fields.Boolean(string="On Leave", default=True)
    payment_ammount = fields.Float(string="Payment Ammount")
    mbti = fields.Text(string="Type")
    contact_no = fields.Char(string="Contact Number")
    employee_photos = fields.Image(
        string="Profile photo", max_width=200, max_height=200)
    age = fields.Integer(string="Age")
    date = fields.Date(string="Today's Date", default=_get_default_date)
    assigned_task = fields.Char(string="Assigned Task")
    supervisor = fields.Char(string="Supervisor")
    assigned_on = fields.Date(string="Assigned On", default=_get_default_date)
    deadline = fields.Date(string="Deadline", compute="_get_compute_deadline")
    worked_days = fields.Date.today()

    # relational field naming covention *_id
    job_position_id = fields.Many2one(
        'bista.job.position', string="Job Position")
    job_position_ids = fields.Many2many(
        'bista.job.position', string="Job Positions")

    @api.model
    def default_get(self, fields):
        values = super(BistaEmployee, self).default_get(fields)
        # values can be modified here
        print(values)
        return values

    @api.depends('assigned_on')
    def _get_compute_deadline(self):
        #print("###################### self.assigned_on ################",self.assigned_on)
        #print("###################### relativedelta (days = 15) ################",relativedelta(days=15))
        if self.assigned_on:
            self.deadline = self.assigned_on + relativedelta(days=15)
        else:
            self.deadline = fields.Date.today()

        # for tree view
        # for obj in self:
        #     obj.deadline = obj.assigned_on + relativedelta(days = 15)

    @api.model
    def create(self, vals):

        # print("vals--------",vals)
        # print("self--------",self)

        if vals['first_name'] == False:
            vals['name'] = vals['last_name']

        if vals['last_name'] == False:
            vals['name'] = vals['first_name']

        if vals['first_name'] != False and vals['last_name'] != False:
            vals['name'] = vals['first_name'] + " " + vals['last_name']

        phone_number = vals['contact_no']

        if len(phone_number) < 11 or len(phone_number) > 11:
            raise ValidationError("Invalid Contact Number")

        if phone_number[:3] != '+88' and len(phone_number) == 11:
            phone_number = "+88" + phone_number
            vals['contact_no'] = phone_number

        if len(phone_number) == 14 and phone_number[:3] != '+88':
            raise ValidationError("Invalid Contact Number")

        result = super(BistaEmployee, self).create(vals)

        # print("vals1-------",vals)
        # print("self1--------",self)
        # print(self)

        # self.name = "Tanim"
        print(result.first_name)
        print(result.last_name)
        print(self)
        # result.first_name = "the freaking monster"
        return result

    def write_my_value(self):
        #self.first_name = "the change name"
        #self.last_name = "Saddick"
        #self.name = self.first_name + " " + self.last_name
        # within search parameter would be list of tupples

        object = self.env['bista.employee'].search(['|', ('last_name', '=', 'Saddick'), ('employee_id', '=', '1')])
        object2 = self.env['bista.employee'].search([('first_name', '=', 'aa')])

        #print('#$#$#$#$')
        #print(object)
        for obj in object:
            obj.age = 100

        for obj in object2:
            print(obj.job_position_id.name)
            job_position_object = self.env['bista.job.position'].browse(obj.job_position_id.id)
            print(job_position_object)



    def view_job_position_detail(self):
        form_view_id = self.env.ref('bista_first_addons.view_bista_employee_job_position_form_simple')
        return{
            'type' : 'ir.actions.act_window',
            'name' : _('Job Position'),
            'res_model' : 'bista.job.position',
            'view_mode' : 'form',
            'res_id' : self.job_position_id.id,
            'view_id' : form_view_id.id,
            'target' : 'new'
        }

    def write(self, vals):
        if 'contact_no' in vals:
            if len(vals['contact_no']) > 14 or len(vals['contact_no']) < 11:
                raise ValidationError(
                    "Wrong Phone number!! : please insert correct phone number.")

            elif len(vals['contact_no']) == 11:
                if vals['contact_no'][0:3] != '+88':
                    vals['contact_no'] = '+88'+vals['contact_no']

                else:
                    raise ValidationError(
                        "Wrong Phone number!! : please insert correct phone number.")

            elif len(vals['contact_no']) == 14:
                if vals['contact_no'][0:3] != '+88':
                    raise ValidationError(
                        "Wrong Phone number!! : please insert correct phone number.")

            else:
                raise ValidationError(
                    "Wrong Phone number!! : please insert correct phone number.")

        if "first_name" in vals or "last_name" in vals:
            # print("____________________________________________")
            if vals.get("first_name") and vals.get("last_name"):
                vals['name'] = vals.get("first_name") + " " + vals.get("last_name")
            elif vals.get("first_name") and not vals.get("last_name"):
                vals['name'] = vals.get("first_name")+" "+self.last_name
            elif vals.get("last_name") and not vals.get("first_name"):
                vals['name'] = self.first_name+" "+vals.get("last_name")

        print(vals)
        result = super(BistaEmployee, self).write(vals)
        return result

    @api.onchange("designation", "experience")
    def onchange_exp_designation(self):
        if self.experience >= 0 and self.designation == "Trainee":
            self.salary = 10000
        elif self.experience >= 2 and self.designation == "Junior_dev":
            self.salary = 30000
        elif self.experience >= 3 and self.designation == "Dev":
            self.salary = 60000
        elif self.experience >= 5 and self.designation == "Senior_dev":
            self.salary = 90000
        elif self.experience >= 7 and self.designation == "ml_engineer":
            self.salary = 90000
        elif self.experience >= 9 and self.designation == "android_dev":
            self.salary = 90000
        elif self.experience >= 10 and self.designation == "pro_manager":
            self.salary = 150000

    @api.onchange('date_of_birth')
    def onchange_date_of_birth(self):
        if self and self.date_of_birth:
            age = (datetime.today().date() - datetime.strptime(str(self.date_of_birth),
                   '%Y-%m-%d').date()) // timedelta(days=365)
            self.age = age
            print(self.age)

    def calculate_salary(self):
        date1 = datetime.strptime(str(self.worked_days), '%Y-%m-%d').date()
        date2 = datetime.strptime(str(self.joining_date), '%Y-%m-%d').date()

        delta_time = relativedelta.relativedelta(date1, date2)
        difference = delta_time.months + (delta_time.years * 12)

        if difference >= 6 and difference < 12:
            new_salary = self.payment_ammount+10000
            raise UserError("current salary is : "+str(new_salary))

        elif difference >= 12:
            new_salary = self.payment_ammount+20000
            raise UserError("current salary is : "+str(new_salary))

        else:
            raise UserError("current salary is : "+str(self.payment_ammount))

    def view_information(self):
        info_message = "Following assignment information \n"+"Assigned task : "+str(self.assigned_task)+"\nAssigned supervior : "+str(
            self.supervisor)+"\nAssigned date : "+str(self.assigned_on)+"\nDeadline : "+str(self.deadline)
        raise UserError(info_message)
