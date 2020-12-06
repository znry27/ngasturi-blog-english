# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime, timedelta

class SalesOrder(models.Model):
    _inherit = 'sale.order'

    def cancel_old_sales_order(self, force_limit=None):
        # days limit
        limit = 7

        # is user fill the force_limit parameter or not
        if force_limit:
            limit = force_limit

        # today date
        date_today = datetime.today()

        # the date that should have been canceled
        cancel_date = date_today - timedelta(days = limit)

        # look for sales orders whose dates match and have not been confirmed
        old_order = self.env['sale.order'].search([('date_order', '<', cancel_date), ('state','in', ['draft','sent'])])
        # cancel sales order that fits the criteria
        old_order.action_cancel()
        
