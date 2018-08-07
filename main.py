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
      generate_template = the_jinja_env.get_template('templates/generate.html')
      
      user_noun = self.request.get('user-noun')
      user_noun2 = self.request.get('user-noun2')
      user_genre = self.request.get('user-genre')
      
      response = urllib2.urlopen("https://api.datamuse.com/words?rel_rhy={}&md=p/".format(user_noun))
      response2 = urllib2.urlopen("https://api.datamuse.com/words?rel_rhy={}&md=p/".format(user_noun2))
      
      json_as_string = response.read()
      json_as_string2 = response2.read()
      
      words_array = json.loads(json_as_string)
      
      words_array2 = json.loads(json_as_string2)
      
      nounarray = []
      nounarray2 = []
      
      for word in words_array:
          try:
              if word["tags"][0] == "n":
                  nounarray.append(word["word"].upper())
          except KeyError:
              pass
          if len(nounarray2) > 8:
              break
           
      for word in words_array2:
          try:
              if word["tags"][0] == "n":
                  nounarray2.append(word["word"].upper())
          except KeyError:
              pass
          if len(nounarray2) > 8:
              break
      print(str(nounarray))
      
      rap = ""
      
      shuffle(nounarray)
      shuffle(nounarray2)
      
      if user_genre == "chill":
         
         chill_txt = open("chill.txt")
         chill_rap = chill_txt.read()
         chill_txt.close()
         
         rap = chill_rap.format(
            noun1 = user_noun.upper(),
            noun2 = user_noun2.upper(),
            noun3 = nounarray2[0],
            noun4 = nounarray[1],
            noun5 = nounarray2[1],
            noun6 = nounarray[2],
            noun7 = nounarray2[2],
            noun8 =  nounarray[3]
            )
         # x = "hello"
         # rap = chill_rap.format(
         #    noun1 = x,
         #    )
      
      render_dict = {"generated_rap" : rap}
      
      print(rap)
      
      
      rendered_template = generate_template.render(render_dict)
      
      self.response.write(rendered_template)

app = webapp2.WSGIApplication([
   ('/', HomePage),
   ('/song', GeneratedPage),
], debug=True)