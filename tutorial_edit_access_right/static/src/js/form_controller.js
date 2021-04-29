odoo.define('tutorial_edit_access_right.form_controller', function (require) {
"use strict";
    // import odoo original form_controller
    var FormController = require('web.FormController');

    // import odoo original dialog, to show the error message
    var Dialog = require('web.Dialog');

    // let's override it
    FormController.include({
    	_onEdit: function () {
	        // print the current model value
	        // so we can make conditions based on it
	        console.log(this);

	        // write the edit access right logic here
	        var is_can_edit = true;
	        if(this.modelName == 'model.three'){
	        	if(this.model.localData[this.handle].data.field_one != 1){
	        		is_can_edit = false
	        	}
	        }

	        if(is_can_edit){
	        	// if user can edit, call the super method
	        	this._super.apply(this, arguments);
	        }else{
	        	// if user can not edit, show a message
	        	Dialog.alert(this, "Sorry you can not edit this document");
	        }
	    },
    });

});