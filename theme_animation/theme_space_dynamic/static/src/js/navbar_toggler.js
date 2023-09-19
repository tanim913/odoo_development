/** @odoo-module */

import publicWidget from 'web.public.widget';

publicWidget.registry.toggleHeaderNavbar = publicWidget.Widget.extend({
    selector: '.navbar-toggler',
    events: {
        // 'click .navbar-toggler': '_onClickToggle'
        'click': '_onClickToggle'
    },

    _onClickToggle(event){

        $(event.currentTarget).toggleClass('opened');
    },
});

