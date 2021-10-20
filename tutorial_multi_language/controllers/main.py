# -*- coding: utf-8 -*-

import odoo
from odoo import http, _
from odoo.http import request
import random

class CustomerPortal(http.Controller):

    @http.route('/customer-portal', type='http', auth="public", website=True)
    def open_customer_portal(self, **kw):
        menus = [
            {'menu_id': 'sale', 'label': _('Sale')},
            {'menu_id': 'purchase', 'label': _('Purchase')}
        ]
        return request.render('tutorial_multi_language.customer_portal', {'menus': menus})

    @http.route('/submit-form', type='json', auth="public", website=False)
    def process_the_form(self, **kw):
        success_message = _('The form is successfully submited')
        error_message = _('Please try again')

        number = random.randint(1,10)

        if number % 2 == 0:
            return {
                'status': 'success',
                'message': success_message
            }
        else:
            return {
                'status': 'failed',
                'message': error_message
            }