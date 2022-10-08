# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions, _

class ModelThree(models.Model):
    _name = 'model.three'
    _description = 'Model Three'

    name = fields.Char()

    def open_model_one(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model One',
            'res_model': 'model.one',
            'view_mode': 'tree,form'
        }

    def open_model_two(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Two',
            'res_model': 'model.two',
            'view_mode': 'tree,form',
            'target': 'fullscreen',
            'domain': [('status','=','new')],
            'context': {'default_name': 'From model three'},
            'limit': 2
        }

    def open_model_two_with_specific_id(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Two',
            'res_model': 'model.two',
            'view_mode': 'form',
            'res_id': 1
        }

    def open_model_two_with_specific_id_and_view_id(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Two',
            'res_model': 'model.two',
            'view_mode': 'form',
            'res_id': self.env.ref('tutorial_action_window.model_two_automatic_created').id,
            'view_id': self.env.ref('tutorial_action_window.model_two_form_view_2').id
        }

    def open_model_two_with_id_and_view_id_from_search(self):
        res_id = self.env['model.two'].search([('name','=','test')],limit=1)
        form_view_id = self.env['ir.ui.view'].search([('model','=','model.two'),('type','=','form'),('priority','>',1)], limit=1)
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Two',
            'res_model': 'model.two',
            'view_mode': 'form',
            'res_id': res_id.id,
            'view_id': form_view_id.id
        }

    def open_model_two_with_views_option(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Two',
            'res_model': 'model.two',
            'views': [
                (self.env.ref('tutorial_action_window.model_two_kanban_view_2').id, 'kanban'),
                (self.env.ref('tutorial_action_window.model_two_tree_view_2').id, 'tree'),
                (self.env.ref('tutorial_action_window.model_two_form_view_2').id, 'form')
            ]
        }

    def open_model_two_with_search_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Two',
            'res_model': 'model.two',
            'view_mode': 'tree,form',
            'search_view_id': [self.env.ref('tutorial_action_window.model_two_search_view_2').id]
        }

    def open_other_record(self):
        res_id = self.env['model.three'].search([('id','!=',self.id)],limit=1)
                
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Three',
            'res_model': 'model.three',
            'view_mode': 'form',
            'res_id': res_id.id
        }

    def open_other_record_as_main_target(self):
        res_id = self.env['model.three'].search([('id','!=',self.id)],limit=1)
                
        return {
            'type': 'ir.actions.act_window',
            'name': 'Model Three',
            'res_model': 'model.three',
            'view_mode': 'form',
            'res_id': res_id.id,
            'target': 'main'
        }

    def open_action_from_xml(self):
        return self.env['ir.actions.act_window']._for_xml_id('tutorial_action_window.action_model_two_open_specific_record')