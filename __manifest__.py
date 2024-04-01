# -*- coding: utf-8 -*-

{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'sequence': -100,
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'wizard/cancel_appointment_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/operation_view.xml',
        'views/odoo_playground_view.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'License': 'LGPL-3',
    'assets': {}
}

