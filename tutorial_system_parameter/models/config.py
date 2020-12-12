# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    allowed_warehouse = fields.Char(string='Allowed Warehouse', config_parameter='allowed_warehouse')
