# -*- coding: utf-8 -*-

{
    'name': "key-value-invoice",
    'version': '16.0.1.0',
    'category': 'key-value-invoice',
    'summary': 'key-value-invoice',
    'description': """
        key-value-invoice
    """,
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
    ],
    'qweb': [],
    'demo': [],
    'installable': True,
    'author': "Alexander Falcon",
    # 'website': "http://www.yourcompany.com",
    'license': 'LGPL-3',
}
