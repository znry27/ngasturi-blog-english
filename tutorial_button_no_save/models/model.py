# -*- coding: utf-8 -*-

from odoo import api, fields, models, exceptions, _

class ModelOne(models.Model):
    _name = 'model.one'

    name = fields.Char()
    model_two_id = fields.One2many('model.two','model_one_id')
    field_one = fields.Integer('Field One')
    field_two = fields.Integer('Field Two')
    field_result = fields.Integer('Field Result')
    result_trigger_field = fields.Char()

    @api.onchange('result_trigger_field')
    def onchange_result_trigger_field(self):
        print('This method will be called in edit mode')        
        for rec in self:
            rec.field_result = rec.field_one + rec.field_two

    def recompute_total(self):
        print('This method will be called in readonly mode')        
        for rec in self:
            rec.field_result = rec.field_one + rec.field_two

    
class ModelTwo(models.Model):
    _name = 'model.two'

    model_one_id = fields.Many2one('model.one')
    model_three_id = fields.One2many('model.three','model_two_id')
    partner = fields.Char('Customer')
    total_order = fields.Float('Total Order', compute='compute_total_order')    
    total_trigger = fields.Char()

    @api.onchange('total_trigger')
    def onchange_total_trigger(self):
        print('This method will be called in modal and modal')
        for model_three in self.model_three_id:
            model_three.total_qty = model_three.qty_one + model_three.qty_two


    def compute_total_order(self):
        for rec in self:
            total = 0
            for m_three in rec.model_three_id:
                total += m_three.total_qty

            rec.total_order = total

    def action_show_order(self):
        view = self.env.ref('tutorial_button_no_save.model_two_form')
        return {
            'name': _('Test Do Not Close Dialog on Button Click'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'model.two',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': self.id,
        }
    


class ModelThree(models.Model):
    _name = 'model.three'

    model_two_id = fields.Many2one('model.two')
    product = fields.Char('Product')
    qty_one = fields.Integer('Qty One')
    qty_two = fields.Integer('Qty Two')
    total_qty = fields.Integer('Total Qty')    