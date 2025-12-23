# -*- coding: utf-8 -*-

from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    key_value_ids = fields.One2many(
        'account.move.key.value',
        'move_id',
        string='Claves y Valores'
    )

class AccountMoveKeyValue(models.Model):
    _name = 'account.move.key.value'
    _description = 'Par Clave-Valor para Factura'

    move_id = fields.Many2one('account.move', string='Factura', ondelete='cascade')
    key = fields.Char(string='Clave', required=True)
    value = fields.Char(string='Valor', required=True)
