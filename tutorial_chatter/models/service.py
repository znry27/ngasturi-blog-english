# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, _

class MyService(models.Model):    
    _name = 'my.service'

    # You are recommended to fill in the _description
    # fill in with an appropriate name, so it will easier when we read the chatter
    _description = 'Service'

    # this part is mandatory if you want the chatter functionality
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    # pay attention to the track_visibility parameter
    name = fields.Char('Service Number', track_visibility='onchange')
    customer = fields.Many2one('res.partner','Customer', track_visibility='onchange')
    date = fields.Date('Date')
    service_detail = fields.One2many('my.service.detail', 'service_id')


class MyServiceDetail(models.Model):    
    _name = 'my.service.detail'

    # You are recommended to fill in the _description
    # fill in with an appropriate name, so it will easier when we read the chatter
    _description = 'Service Detail'

    # this part is mandatory if you want the chatter functionality
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']

    # pay attention to the track_visibility parameter
    product = fields.Many2one('product.product', 'Product', track_visibility='onchange')
    customer_complaint = fields.Char('Customer Complaint', track_visibility='onchange')
    warranty = fields.Boolean('Warranty')
    service_id = fields.Many2one('my.service')