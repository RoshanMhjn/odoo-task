{
    'name': 'Employee Asset Request',
    'version': '1.0.0',
    'category': 'Human Resources',
    'summary': 'Request and manage company assets',
    'description': """
        Employee Asset Request
        =======================
        Allows employees to request company assets such as
        laptops, monitors, phones, keyboards, and mice.
    """,
    'author': 'Roshan Maharjan',
    'license': 'LGPL-3',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_asset_request_views.xml',
    ],
    'installable': True,
    'application': True,
}