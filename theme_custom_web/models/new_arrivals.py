from odoo import models, fields

class NewArrivals(models.Model):
    _name = 'new.arrivals'
    _description = "New Arrival Collection"

    product_id  = fields.Many2one('product.product', string="Product")
    product_name = fields.Char(related='product_id.name', string="Name")
    product_image = fields.Binary(related='product_id.image_1920')
    product_price = fields.Float(related='product_id.standard_price', string="Price")
    description = fields.Text() 