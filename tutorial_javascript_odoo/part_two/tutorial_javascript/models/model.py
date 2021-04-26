# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _

class Tutorial(models.Model):
    _name = 'tutorial.javascript'

    field_one = fields.Integer('Field One')

    