{
    'name': 'Custom Web Theme',
    'description': 'Custom Web Theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
        'views/new_arrivals_views.xml',
        'views/snippets/jewelry_making.xml',
        'views/snippets/snippets.xml',
    ],
    'images': [
    ],
    'snippet_lists': {
    },
'assets':{
        'web.assets_frontend': [
            'theme_custom_web/static/src/scss/styles.scss',
            'theme_custom_web/static/src/scss/making_jewelry.scss'
        ],
        'web._assets_primary_variables': [
            "theme_custom_web/static/src/scss/primary_variables.scss",
        ]
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}