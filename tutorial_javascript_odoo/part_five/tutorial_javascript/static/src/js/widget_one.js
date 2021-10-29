odoo.define('tutorial_javascript.widget_one', function (require) {
"use strict";
    // import the required object to create a widget
    var AbstractField = require('web.AbstractField');
    var FieldRegistry = require('web.field_registry');
    var field_utils = require('web.field_utils');
    var session = require('web.session');
    var Dialog = require('web.Dialog');
    var view_dialogs = require('web.view_dialogs');

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
            // Dialog.alert(
            //     this,
            //     "Are you sure you want to fill this field with a value of 0 ?",
            //     {
            //         onForceClose: function(){
            //             console.log("The user closes the dialog forcibly, by clicking on the button with the close icon");
            //         },
            //         confirm_callback: function(){
            //             console.log("The user clicks on the OK button");
            //             self._setValue("0");
            //         }
            //     }
            // );    

            // Dialog.confirm(
            //     this,
            //     "Are you sure you want to fill this field with a value of 1000 ?",
            //     {
            //         onForceClose: function(){
            //              console.log("The user closes the dialog forcibly, by clicking on the button with the close icon");
            //         },
            //         confirm_callback: function(){
            //             console.log("The user clicks on the OK button");
            //             self._setValue("1000");
            //         },
            //         cancel_callback: function(){
            //             console.log("The user clicks on the Cancel button");
            //         }
            //     }
            // );   

            // new view_dialogs.FormViewDialog(this, {
            //     res_model: 'sale.order', // the model name           
            //     res_id: 1, // the primary key of the model
            //     title: "Sale Order with ID of 1", // dialog title, optional
            //     on_saved: function (record) { // the action that will be executed if user clicks the Save button
            //         console.log("The user clicks the Save button");
            //     }
            // }).open();

            
            new view_dialogs.SelectCreateDialog(this, {
                res_model: 'sale.order', // the model name     
                title: "Select the Sales Order", // dialog title, optional
                domain: [['state','!=', 'draft']], // domain to limit the record that can be selected, optional
                no_create: true, // an option to make sure that user can not create a new record, optional
                on_selected: function (records) {
                    var record_ids = records.map(function(item){
                        return item['id'];
                    });
                    self._rpc({
                        model: self.attrs.relatedModel,
                        method: self.attrs.modifiers.relatedAction,
                        args: [record_ids,0,0],
                        kwargs: {value_3: 0, value_4: 0}                
                    }).then(function(result){
                        self._setValue(result.toString());
                    });   
                }
            }).open();      
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
