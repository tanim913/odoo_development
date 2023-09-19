odoo.define('theme_space_dynamic.preloader', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');


    publicWidget.registry.PagePreloader = publicWidget.Widget.extend({
        selector: '#wrap',
        /**
         * @override
         */
        start: function () {
            return this._super.apply(this, arguments).then(function () {
                $('#js-preloader').addClass('loaded');
            });
        },
    });
    return publicWidget.registry.PagePreloader;
});
