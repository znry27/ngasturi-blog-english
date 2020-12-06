# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductRepair(models.Model):
    _name = 'product.repair'
    # we must inherit mail.thread model if we want to be able to send email from our model
    _inherit = ['mail.thread'] 
    _description = "Product Repair"

    product_id = fields.Many2one('product.product', string='Product')
    partner_id = fields.Many2one('res.partner', string='Customer')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('finish', 'Finished')
    ], default='draft')


    def send_finish_email(self):
        # search the email template based on external id
        template_id = self.env['ir.model.data'].xmlid_to_res_id('tutorial_email.product_repair_finish_email_template', raise_if_not_found=False)
        if template_id:
            for rec in self:
                rec.with_context(force_send=True).message_post_with_template(template_id, email_layout_xmlid="tutorial_email.message_no_odoo_branding")