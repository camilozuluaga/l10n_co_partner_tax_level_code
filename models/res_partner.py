# -*- coding: utf-8 -*-
# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _
_logger = logging.getLogger(__name__)



class Respartner(models.Model):


	_inherit = 'res.partner'


	tax_level_code_id = fields.Many2one('tax.level.code', string = u'Tax Level')