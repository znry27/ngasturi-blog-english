odoo.define('tutorial_javascript.widget_one', function (require) {
"use strict";
    // import the required object to create a widget
    var AbstractField = require('web.AbstractField');
    var FieldRegistry = require('web.field_registry');

    // create an object with any name
    // don't forget to extend to the web.AbstractField object or its child
    var WidgetOne = AbstractField.extend({
        template: 'WidgetOneTemplate', // isi nama template yang telah dibuat untuk mengatur tampilan/view widget
    });

    // register the widget to web.field_registry object
    // so we can use our widget in odoo's view/xml file
    // with the code like below
    // <field name="field_one" widget="widget_one" />
    // the 'widget_one' name is up to you, as long as it's always connected/without spaces
    FieldRegistry.add('widget_one', WidgetOne);

    // return the widget object
    // so it can be inherited or overridden by another module
    return WidgetOne;

});