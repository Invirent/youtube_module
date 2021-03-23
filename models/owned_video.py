from odoo import models, fields, api

class YoutubeContent(models.Model):
    _name="youtube.content"

    name=fields.Char(string="Name of the Video")
    youtube_id=fields.Char(string="Id of the Video", readonly=False)
    youtube_link=fields.Char(string="Link to the youtube video", readonly=False)
    video_date=fields.Date(string="Release Date",readonly=False)
    viewer_total=fields.Integer(string="Total Viewer",readonly=False)
    like_count=fields.Integer(string="Like Count")
    dislike_count=fields.Integer(string="Dislike Count")
    link_redirect=fields.Char(string="Video URL Redirect")
    youtube_desc=fields.Char(string="Youtube Desc....")
    

