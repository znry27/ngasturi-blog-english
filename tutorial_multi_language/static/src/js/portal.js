odoo.define('tutorial_multi_language.portal', function (require) {
'use strict';

    var publicWidget = require('web.public.widget');
    var core = require('web.core');
    var qweb = core.qweb;
    var _t = core._t;

    publicWidget.registry.MultiLangPortal = publicWidget.Widget.extend({
        selector: '.portal-container',
        events: {
            'click .menu-item': 'openMenu',
            'click .btn-submit': 'submitForm',
            'click .dialog-close': 'closeDialog'
        },
        xmlDependencies: [
            '/tutorial_multi_language/static/src/xml/templates.xml'
        ],
        openMenu: function(e){
            e.preventDefault();
            e.stopPropagation();
            $(".portal-content").empty();

            var menu_id = $(e.currentTarget).data("menu-id");

            if(menu_id == 'sale'){
                this.$el.find(".portal-content").append($(qweb.render('sale')));
            }else  if(menu_id == 'purchase'){
                this.$el.find(".portal-content").append($(qweb.render('purchase')));
            }
        },
        submitForm: function(e){
            e.preventDefault();
            e.stopPropagation();

            this._rpc({
                route: 'submit-form'
            }).then(function(result){
                $(".portal-container").append($(qweb.render('alert', {message: _t(result['message'])})));
            });
        },
        closeDialog: function(){
            $(".dialog-container").remove();
        },
    });

});