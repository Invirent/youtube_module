# -*- coding: utf-8 -*-
# from odoo import http


# class YoutubeModule(http.Controller):
#     @http.route('/youtube_module/youtube_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/youtube_module/youtube_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('youtube_module.listing', {
#             'root': '/youtube_module/youtube_module',
#             'objects': http.request.env['youtube_module.youtube_module'].search([]),
#         })

#     @http.route('/youtube_module/youtube_module/objects/<model("youtube_module.youtube_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('youtube_module.object', {
#             'object': obj
#         })
