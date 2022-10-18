# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bista First Module',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 1,
    'author': 'Bista-Training-Team-BD-2022',
    'summary': 'Bista employee information',
    'description': "Bista employee information",
    'website': 'https://www.odoo.com/app/employees',
    'depends': [
        'base_setup',
    ],
    'data': [
        # 'security/hr_security.xml',
        'security/ir.model.access.csv',
        'views/bista_employee_views.xml',
        'views/job_position_views.xml',
        # 'views/hr_plan_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
