# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name': 'l10n_co partner tax level code',
	'version': '1.0',
	'website': '',
	'category': 'Localizacion',
	'summary': 'l10n_co partner tax level code',
	'description': """
	

	""",
	'depends': [
		'account',
		'l10n_co_partner_vat'
	],
	'data': [
		'data/tax_level_code_data.xml',
		'views/tax_level_code.xml',
		'views/res_partner.xml',
		'security/ir.model.access.csv',
		
	],
	'installable': True,
	'auto_install': False,
	'application': True,
}
