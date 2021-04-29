# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _

class ModelOne(models.Model):
    _name = 'model.one'

    name = fields.Char()
    field_one = fields.Integer('Field One')
    field_two = fields.Integer('Field Two')

    def action_change_field(self):
        for rec in self:
            rec.field_two = 5

    
class ModelTwo(models.Model):
    _name = 'model.two'

    name = fields.Char()
    field_one = fields.Integer('Field One')
    field_two = fields.Integer('Field Two')

    def write(self, vals):
        if 'ignore_write_access' not in self._context:
            if self.field_one != 1:
                raise exceptions.UserError('You can not edit this document')

        return super(ModelTwo,self).write(vals)

    def action_change_field(self):
        for rec in self:
            rec.with_context({'ignore_write_access': 1}).field_two = 5


class ModelThree(models.Model):
    _name = 'model.three'

    name = fields.Char()
    field_one = fields.Integer('Field One')
    field_two = fields.Integer('Field Two')

    def action_change_field(self):
        for rec in self:
            rec.field_two = 5


class ModelFour(models.Model):
    _name = 'model.four'

    name = fields.Char()
    field_one = fields.Integer('Field One')
    field_two = fields.Integer('Field Two')

    def write(self, vals):
        if 'from_ui' in self._context:
            if self.field_one != 1:
                raise exceptions.UserError('You can not edit this document')

        return super(ModelFour,self).write(vals)

    def action_change_field(self):
        for rec in self:
            rec.field_two = 5

    