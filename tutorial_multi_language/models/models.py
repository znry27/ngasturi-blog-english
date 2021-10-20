# -*- coding: utf-8 -*-

from odoo import api, fields, models

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    # @classmethod
    # def _get_translation_frontend_modules_name(cls):
    #     mods = super(IrHttp, cls)._get_translation_frontend_modules_name()
    #     return mods + ['tutorial_multi_language']

class IrTranslation(models.Model):
    _inherit = "ir.translation"
    
    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        res = super(IrTranslation, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)
        # for r in res:
        #     if r.get('src','') == 'Save':
        #         a = 8 / 0
        return res