# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _

class Tutorial(models.Model):
    _name = 'tutorial.javascript'

    field_one = fields.Integer('Field One')
    field_two = fields.Integer('Field Two')
    field_three = fields.Integer('Field Three')


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_last_order_amount(self, value_1, value_2, value_3=3, value_4=4):
        print('get_last_order_amount=====called=======')
        print(self)
        print(value_1)
        print(value_2)
        print(value_3)
        print(value_4)
        value = 0
        for order in self:
            print('oder_id====', order.id)
            print('customer====', order.partner_id.name)
            print('amount====', order.amount_total)
            value += order.amount_total
        return value

    
