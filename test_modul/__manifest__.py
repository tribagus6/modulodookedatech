{
    'name': 'KeDATech Test',
    'version': '16.0.1.0',
    'category': 'purcase',
    'author': 'Tri Bagus',
    'website': 'https://www.linkedin.com/in/tri-bagus-pamungkas-98a68524b/',
    'summary': 'To meet test requirements',
    'description': """
        This is custom modul for test requirements from KeDATech
    """,
    'depends': ['web','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/registrasi_material_view.xml',
        'views/registrasi_material_action.xml',
        'views/registrasi_material_menuitem.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',

}