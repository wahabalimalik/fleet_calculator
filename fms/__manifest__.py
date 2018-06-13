# -*- coding: utf-8 -*-
{
    'name': "fms",

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
        "account_accountant",
        "account_cancel",
        "fleet",
        "hr",
        "purchase",
        "sale",
        "base_geoengine",
        "account_operating_unit"
    ],
    'data': [
        'views/fms_view.xml',
        'views/fms_fuel.xml',
        'views/fms_route_management.xml',
        'views/fms_unit_kit_view.xml',
        'views/fms_shipment_view.xml',
        'views/fms_accident_management.xml',
        'views/fms_service_management.xml',
        'views/fms_contracts_management.xml',
        'views/fms_inventory_management.xml',
        'views/fms_general_reports.xml',
        'views/fleet_vehicle_view.xml',
        'views/fleet_vehicle_expense_view.xml',
        'views/fleet_vehicle_log_fuel_view.xml',
        'views/fms_tyre_view.xml',
        'views/hr_employee_view.xml',
    ],
    "application": True,
    "installable": True, 
}