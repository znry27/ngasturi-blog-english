# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, _

class ModelTwo(models.Model):
    _name = 'model.two'
    _description = 'Model Two'

    name = fields.Char()
    status = fields.Selection([
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('closed', 'Closed')
    ], default='new')
    description = fields.Text()