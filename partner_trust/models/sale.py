# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        # If partner is not blacklisted, call super, it means that the sale order can be confirmed

        # if there is a context approve_blacklisted_customer_order it means that this method
        # is called from the sale.trust.wizard transient model and the user have
        # 'Approve sale order of blacklisted customer' access rights, so the sale order can be confirmed
        if self.partner_id.trust_state == 'trusted' or 'approve_blacklisted_customer_order' in self._context:
            super(SaleOrder, self).action_confirm()

        else:
            # partners is blacklisted
            # create transient model record with the value of order_id is the current sale order id
            # by inserting the order_id field, later in the sale.trust.wizard transient model
            # we can call the action_confirm method to confirm this sales order
            wizard_id = self.env['sale.trust.wizard'].create({'order_id': self.id})
            return {
                'name': _('Blacklisted Customer'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'sale.trust.wizard',
                'res_id': wizard_id.id,
                'target': 'new',
            }