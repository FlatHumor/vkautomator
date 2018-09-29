# -*- coding: utf-8 -*-
from odoo import http

# class Vkautomator(http.Controller):
#     @http.route('/vkautomator/vkautomator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vkautomator/vkautomator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vkautomator.listing', {
#             'root': '/vkautomator/vkautomator',
#             'objects': http.request.env['vkautomator.vkautomator'].search([]),
#         })

#     @http.route('/vkautomator/vkautomator/objects/<model("vkautomator.vkautomator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vkautomator.object', {
#             'object': obj
#         })