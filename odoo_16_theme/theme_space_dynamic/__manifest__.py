{
    'name': 'Space Dynamic Theme',
    'description': 'Space Dynamic website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['dynamic_theme_base','website'],
    'data': [
    ],
    'images': [
    ],
    'snippet_lists': {
    },
    'assets': {
        'web.assets_frontend': [
            '/theme_space_dynamic/static/src/scss/header/space_dynamic_header.scss',
            '/theme_space_dynamic/static/src/scss/footer/space_dynamic_footer.scss',
            '/theme_space_dynamic/static/src/scss/template.scss',
            '/theme_space_dynamic/static/src/scss/animations.scss',
            '/theme_space_dynamic/static/src/js/navbar_toggler.js',
        ],
        'web._assets_primary_variables': [
            ("prepend", "theme_space_dynamic/static/src/scss/fonts.scss"),
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
