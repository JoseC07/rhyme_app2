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
        self.response.write("Hello World!")
   


class GeneratedPage(webapp2.RequestHandler):
    def get(self):
        
        self.response.write("Hello World! generate page")
        
    



app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/generate', GeneratedPage),
], debug=True)


