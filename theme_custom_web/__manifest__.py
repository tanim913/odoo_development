{
    'name': 'Custom Web Theme',
    'description': 'Custom Web Theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/homepage.xml',
    ],
    'images': [
    ],
    'snippet_lists': {
    },
'assets':{
        'web.assets_frontend': [
            'theme_custom_web/static/src/scss/styles.scss'
        ],
        'web._assets_primary_variables': [
            "theme_custom_web/static/src/scss/primary_variables.scss",
        ]
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}