# -*- coding: utf-8 -*-

from odoo import http
# import odoo controller
from odoo.addons.web.controllers.main import DataSet

# let's override it
class DataSetInherit(DataSet):

    @http.route(['/web/dataset/call_kw', '/web/dataset/call_kw/<path:path>'], type='json', auth="user")
    def call_kw(self, model, method, args, kwargs, path=None):
        # add new unique context
        kwargs['context']['from_ui'] = 1
        # call the super method
        return super(DataSetInherit,self)._call_kw(model, method, args, kwargs)
