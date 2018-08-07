import webapp2
from random import shuffle
import jinja2
import os


#libraries for APIs
import json
import urllib2


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
   
   def post(self):
      json_response = urllib2.urlopen("https://api.datamuse.com/words?rel_rhy={}&md=p/".format(noun))
      
      
      
      generate_template = the_jinja_env.get_template('templates/generate.html')
      self.response.write(generate_template.render())
       

app = webapp2.WSGIApplication([
   ('/', HomePage),
   ('/song', GeneratedPage),
], debug=True)