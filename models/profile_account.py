from odoo import models, fields, api

class ProfileAccount(models.Model):
    _inherit='youtube.content'

    channel_name = fields.Char(string = "Channel Name")
    channel_date = fields.Datetime(string = "Channel created date")
    subs_count=fields.Integer(string = "Subscriber Count")
    playlist_count = fields.Integer(string="Playlist count")
    youtube_id = fields.Char(string="Your Youtube Ids")