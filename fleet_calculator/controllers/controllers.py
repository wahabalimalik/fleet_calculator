# -*- coding: utf-8 -*-
from odoo import http

# class FleetCalculator(http.Controller):
#     @http.route('/fleet_calculator/fleet_calculator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fleet_calculator/fleet_calculator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fleet_calculator.listing', {
#             'root': '/fleet_calculator/fleet_calculator',
#             'objects': http.request.env['fleet_calculator.fleet_calculator'].search([]),
#         })

#     @http.route('/fleet_calculator/fleet_calculator/objects/<model("fleet_calculator.fleet_calculator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fleet_calculator.object', {
#             'object': obj
#         })