from odoo import models, fields, api

class YoutubeContent(models.Model):
    _name="youtube.content"

    name=fields.Char(string="Name of the Video")
    youtube_id=fields.Char(string="Id of the Video", readonly=False)
    youtube_link=fields.Char(string="Link to the youtube video", readonly=False)
    video_date=fields.Datetime(string="Release Date",readonly=False)
    

