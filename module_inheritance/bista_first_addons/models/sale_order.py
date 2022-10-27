
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contact_no = fields.Char(string="Contact Number")
    secondary_contact_no = fields.Char(string="Secondary Contact Number")

    def action_confirm(self):
        if not self.validity_date:
            raise UserError("Enter expiration Date")

        for line in self.order_line:
            if line.price_unit <= 0:
                raise UserError("Please set unit price for product '{}'".format(line.product_id.name))

            if line.product_uom_qty <= 0:
                raise UserError("Please set quantity for product '{}'".format(line.product_id.name))

        res = super(SaleOrder, self).action_confirm()

        return res

    @api.onchange("partner_id")
    def onchange_partner_id_add_contact_info(self):
        # if self and self.partner_id:
            print("########### 111111111 #################")
            if self.partner_id.phone:
                print("############################")
                self.contact_no = self.partner_id.phone
            else:
                self.contact_no = False

            if self.partner_id.secondary_contact_no:
                self.secondary_contact_no = self.partner_id.secondary_contact_no
            else:
                self.secondary_contact_no = False

