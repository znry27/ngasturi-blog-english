# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class TutorialController(http.Controller):

    @http.route(['/tutorial/amount'], type='json', auth='user')
    def get_amount(self, **kwargs):
        print('Controller=====/tutorial/amount=====called')
        print(kwargs)
        return 20000