# -*- coding: utf-8 -*-
{
    'name': "fms groups",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'FMS',
    'version': '0.1',
    'depends': [
        "fms",
    ],
    'data': [
        'security/fms_groups.xml',
        'security/ir.model.access.csv',
    ],
    "application": True,
    "installable": True,
}