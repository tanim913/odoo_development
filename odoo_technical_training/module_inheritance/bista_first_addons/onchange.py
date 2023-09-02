# @api.onchange("partner_id")
#     def onchange_partner_id_add_phone_no(self):
#         if self and self.partner_id :
#             # partner_id is a many2one field so it always refers with id. So no need to use search
#             if self.partner_id.phone:
#                 self.customer_phone_no = self.partner_id.phone
#             elif self.partner_id.mobile:
#                 self.customer_phone_no = self.partner_id.mobile
#             else:
#                 #if dont use false then the field wont change if there is no number and once filled.
#                 self.customer_phone_no = False
#             if self.partner_id.secondary_contact:
#                 self.customer_secondary_contact=self.partner_id.secondary_contact
#             else:
#                 self.customer_secondary_contact=False
