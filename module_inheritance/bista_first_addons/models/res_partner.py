
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection([('male', "Male"), ('female', "Female"), ('other', "Other")], string = "Gender")
    secondary_contact_no = fields.Char(string="Secondary Contact Number")
    
    @api.model
    def create(self, values):
        if not values.get('gender'): 
            raise UserError("Gender field is Empty!")
        res = super(ResPartner, self).create(values)
        return res