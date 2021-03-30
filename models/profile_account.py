from odoo import models, fields, api

class YoutubeAccount(models.Model):
    _name= 'youtube.profile'

    channel_name = fields.Char(string = "Channel Name")
    channel_date = fields.Datetime(string = "Channel created date")
    subs_count=fields.Integer(string = "Subscriber Count")
    playlist_count = fields.Integer(string="Playlist count")
    redirect_url=fields.Char(string="")
    oauth_client_id=fields.Char(string="Client Ids", help="To Obtain this ,please visit https://console.cloud.google.com/ , The Full documentation in making Oauth code is in documentation folder")
    oauth_client_secret=fields.Char(string="Client Secret",help="To Obtain this ,please visit https://console.cloud.google.com/ , The Full documentation in making Oauth code is in documentation folder")
    