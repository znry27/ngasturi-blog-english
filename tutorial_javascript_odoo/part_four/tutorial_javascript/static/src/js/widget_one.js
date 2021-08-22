odoo.define('tutorial_javascript.widget_one', function (require) {
"use strict";
    // import the required object to create a widget
    var AbstractField = require('web.AbstractField');
    var FieldRegistry = require('web.field_registry');
    var field_utils = require('web.field_utils');
    var session = require('web.session');

    // import qweb to render a view
    var core = require('web.core');
    var qweb = core.qweb;

    // create an object with any name
    // don't forget to extend to the web.AbstractField object or its child
    var WidgetOne = AbstractField.extend({
        step: 1, // default value, if user not configure it in xml file
        template: 'WidgetOneTemplate', // fill with the template name that will be rendered by odoo
        events: { // list of event, like jquery event
            'click .btn-minus': 'btn_minus_action',
            'click .btn-plus': 'btn_plus_action',
            'click .btn-dollar': 'btn_dollar_action', // additional in tutorial part four
        },
        init: function () {
            // the 'init' method is called first
            this._super.apply(this, arguments);
            if(this.nodeOptions.step){
                // if user configure the 'step' value in xml file
                // change the default value to user desired value
                this.step = this.nodeOptions.step;
            }
        },
        btn_minus_action: function(){
            var new_value = this.value - this.step;
            this._setValue(new_value.toString());            
        },
        btn_plus_action: function(){
            console.log(this);
            var new_value = this.value + this.step;
            this._setValue(new_value.toString());
        },
        btn_dollar_action: function(){
            var self = this;
            // this._rpc({
            //     model: this.attrs.relatedModel,
            //     method: this.attrs.modifiers.relatedAction,
            //     args: [[1,2],100,200],
            //     kwargs: {value_4: 4000}                
            // }).then(function(result){
            //     self._setValue(result.toString());
            // });   


            session.rpc(
                '/tutorial/amount',
                {
                    'oder': [1,2]
                }
            ).then(function(result){
                self._setValue(result.toString());
            });            
        },
        _render: function () {
            // re-render the view if the field value is changed
            // format the value to include the thousand separator
            var formated_value = field_utils.format[this.formatType](this.value);
            this.$el.html($(qweb.render(this.template, {'widget': this, 'formated_value': formated_value})));
            this.$el.find('.btn-copy').click(function(){
                // we can also use this code
                // self.$el.find('input').val();
                // if we want access the field one value with jquery
                // by accessing the widget element
                var field_one_val = self.value;
                var field_two_val = $('[name=field_two]').val();
                var field_three_val = field_one_val + parseInt(field_two_val);
                self.trigger_up('field_changed', {
                    dataPointID: self.dataPointID,
                    viewType: self.viewType,
                    changes: {'field_three': field_three_val},
                });
            });
        },
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
