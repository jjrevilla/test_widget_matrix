# -*- coding: utf-8 -*-
from openerp import http

# class Mymodules/testWidgetMatrix(http.Controller):
#     @http.route('/mymodules/test_widget_matrix/mymodules/test_widget_matrix/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mymodules/test_widget_matrix/mymodules/test_widget_matrix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mymodules/test_widget_matrix.listing', {
#             'root': '/mymodules/test_widget_matrix/mymodules/test_widget_matrix',
#             'objects': http.request.env['mymodules/test_widget_matrix.mymodules/test_widget_matrix'].search([]),
#         })

#     @http.route('/mymodules/test_widget_matrix/mymodules/test_widget_matrix/objects/<model("mymodules/test_widget_matrix.mymodules/test_widget_matrix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mymodules/test_widget_matrix.object', {
#             'object': obj
#         })