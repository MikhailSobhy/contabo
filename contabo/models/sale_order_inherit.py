from odoo import models,api,fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contabo = fields.Char()
    server_text = fields.Char()