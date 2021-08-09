# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class IrUiView(models.Model):
	_inherit = 'ir.ui.view'

	@api.constrains('arch_db')
	def _check_xml(self):
		context = dict(self._context)
		context['load_all_views'] = True

		return super(IrUiView, self.with_context(context))._check_xml()