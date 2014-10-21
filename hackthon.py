#-*- coding: utf-8 -*-
import  webapp2, cgi
from google.appengine.ext import db
from jinja2 import Environment, PackageLoader, Template, FileSystemLoader
jinja_env = Environment(loader=FileSystemLoader('templates'), autoescape=True)

class Handler(webapp2.RequestHandler):
    """docstring for Handler"""
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        print "here"
        self.write(self.render_str(template, **kw))
    # def post(self):
    #     subject = self.request.get("subject")
    #     content = self.request.get("content")

class NewsPage(Handler):
    """docstring for NewsPage"""
    def get(self):
        self.render("new.html")

class ApplyPage(Handler):
    """docstring for NewsPage"""
    def get(self):
        self.render("apply.html")

class InforPage(Handler):
    """docstring for NewsPage"""
    def get(self):
        self.render("infor.html")

app = webapp2.WSGIApplication([('/', NewsPage), ('/Infor', InforPage), ('/apply', ApplyPage)], debug=True)