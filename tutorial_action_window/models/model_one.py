# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, _

class ModelOne(models.Model):
    _name = 'model.one'
    _description = 'Model One'

    name = fields.Char()
    description = fields.Text()
    detail_ids = fields.One2many('model.one.detail', 'header_id')

class ModelOneDetail(models.Model):
    _name = 'model.one.detail'
    _description = 'Model One Detail'

    name = fields.Char()
    value = fields.Float()
    header_id = fields.Many2one('model.one')