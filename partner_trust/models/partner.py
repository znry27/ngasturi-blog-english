# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Partner(models.Model):
    _inherit = 'res.partner'

    trust_state = fields.Selection([
            ('trusted', 'Trusted'),
            ('blacklisted', 'Blacklisted')
        ], string='Trust Status', default='trusted')