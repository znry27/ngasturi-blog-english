# -*- coding: utf-8 -*-
# import the default odoo module
from odoo import api, fields, models, exceptions, _

# create a new class
# the class name is up to you, but must inherit to Model class
class sale_order(models.Model):
    # use _inherit if we want to override the existing class
    # the sale.order model is exist in the original odoo code
    # if the model does not exist or the module not yet installed
    # it will cause an error
    _inherit = 'sale.order'

    # create a new database table column with varchar data type and mandatory
    # we will discuss the other data type in another article
    middleman = fields.Char("Middleman", required=True)