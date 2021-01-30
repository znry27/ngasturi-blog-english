# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import content_disposition, request
import io
import xlsxwriter
    


class SaleExcelReportController(http.Controller):
    @http.route([
        '/sale/excel_report/<model("ng.sale.wizard"):wizard>',
    ], type='http', auth="user", csrf=False)
    def get_sale_excel_report(self,wizard=None,**args):
        # the wizard parameter is the primary key that odoo sent 
        # with the get_excel_report method in the ng.sale.wizard model
        # contains salesperson, start date, and end date

        # create a response with a header in the form of an excel file
        # so the browser will immediately download it
        # The Content-Disposition header is the file name fill as needed
        
        response = request.make_response(
                    None,
                    headers=[
                        ('Content-Type', 'application/vnd.ms-excel'),
                        ('Content-Disposition', content_disposition('Sales Report in Excel Format' + '.xlsx'))
                    ]
                )

        # create workbook object from xlsxwriter library
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})

        # create some style to set up the font type, the font size, the border, and the aligment
        title_style = workbook.add_format({'font_name': 'Times', 'font_size': 14, 'bold': True, 'align': 'center'})
        header_style = workbook.add_format({'font_name': 'Times', 'bold': True, 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'center'})
        text_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'left'})
        number_style = workbook.add_format({'font_name': 'Times', 'left': 1, 'bottom':1, 'right':1, 'top':1, 'align': 'right'})

        # loop all selected user/salesperson
        for user in wizard.user_id:
            # create worksheet/tab per salesperson 
            sheet = workbook.add_worksheet(user.name)
            # set the orientation to landscape
            sheet.set_landscape()
            # set up the paper size, 9 means A4
            sheet.set_paper(9)
            # set up the margin in inch
            sheet.set_margins(0.5,0.5,0.5,0.5)

            # set up the column width
            sheet.set_column('A:A', 5)
            sheet.set_column('B:E', 15)

            # the report title
            # merge the A1 to E1 cell and apply the style font size : 14, font weight : bold
            sheet.merge_range('A1:E1', 'Sales Report in Excel Format', title_style)
            
            # table title
            sheet.write(1, 0, 'No.', header_style)
            sheet.write(1, 1, 'Document', header_style)
            sheet.write(1, 2, 'Date', header_style)
            sheet.write(1, 3, 'Customer', header_style)
            sheet.write(1, 4, 'Total', header_style)

            row = 2
            number = 1

            # search the sales order  
            orders = request.env['sale.order'].search([('user_id','=',user.id), ('date_order','>=', wizard.start_date), ('date_order','<=', wizard.end_date)])
            for order in orders:
                # the report content
                sheet.write(row, 0, number, text_style)
                sheet.write(row, 1, order.name, text_style)
                sheet.write(row, 2, str(order.date_order), text_style)
                sheet.write(row, 3, order.partner_id.name, text_style)
                sheet.write(row, 4, order.amount_total, number_style)

                row += 1
                number += 1

            # create a formula to sum the total sales
            sheet.merge_range('A' + str(row+1) + ':D' + str(row+1), 'Total', text_style)
            sheet.write_formula(row, 4, '=SUM(E3:E' + str(row) + ')', number_style)

        # return the excel file as a response, so the browser can download it
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()

        return response