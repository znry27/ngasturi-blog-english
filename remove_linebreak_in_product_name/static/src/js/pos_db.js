odoo.define('remove_linebreak_in_product_name.pos_db', function (require) {
    "use strict";
    var PosDB = require('point_of_sale.DB');

    PosDB.include({
        _product_search_string: function(product){
            var result = this._super.apply(this, arguments);
            return result.replace(/(\r\n|\n|\r)/gm, ' ') + '\n';
        },
    });

});