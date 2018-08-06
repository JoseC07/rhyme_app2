import webapp2
from random import shuffle
import jinja2
import os


#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(about_template.render())
   


class GeneratedPage(webapp2.RequestHandler):
    def get(self):
        
        self.response.write("Here's your rap!")
        
    



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/generate', GeneratedPage),
], debug=True)


