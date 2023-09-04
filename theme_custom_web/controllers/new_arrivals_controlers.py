from odoo import http


class NewArrivalsControllers(http.Controller):

    @http.route('/new_arrivals_list/', auth="public", type="json", methods=['POST'])
    def all_cities(self):
        product_info = ['product_id', 'product_name', 'product_price', 'product_image']
        # print("-----------------> ", product_info)
        new_products = http.request.env['new.arrivals'].search_read([], product_info)
        # print("-----------------> ", new_products)
        return new_products
