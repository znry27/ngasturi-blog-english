# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        # read the system parameter with key of 'allowed_warehouse'
        # if not exist, it will return an empty string
        # then split based on the comma character to convert it into a list

        allowed_warehouse = self.env['ir.config_parameter'].get_param('allowed_warehouse', '').split(',')
        
        # because the list value is stored in string, convert it to an integer
        allowed_warehouse = list(map(lambda x: int(x), allowed_warehouse))

        # check the warehouse field that selected by the user, is it in the list of warehouses that are allowed or not
        if vals.get('warehouse_id', False) not in allowed_warehouse:
            raise exceptions.ValidationError('You are not allowed to create the sales order in this warehouse !')


        return super(SaleOrder, self).create(vals)


    def write(self, vals):
        # read the system parameter with key of 'allowed_warehouse'
        # if not exist, it will return an empty string
        # then split based on the comma character to convert it into a list

        allowed_warehouse = self.env['ir.config_parameter'].get_param('allowed_warehouse', '').split(',')

        # because the list value is stored in string, convert it to an integer
        allowed_warehouse = list(map(lambda x: int(x), allowed_warehouse))

        # check the warehouse field that selected by the user, is it in the list of warehouses that are allowed or not
        if vals.get('warehouse_id', False) not in allowed_warehouse:
            raise exceptions.ValidationError('You are not allowed to create the sales order in this warehouse !')


        return super(SaleOrder, self).write(vals)

    def unlink(self):        
        for rec in self:
            deleted = int(self.env['ir.config_parameter'].get_param('deleted_sale_order', '0')) + 1
            self.env['ir.config_parameter'].set_param('deleted_sale_order', deleted)

        return super(SaleOrder, self).unlink()