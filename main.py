#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IndexHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title': 'HOME','page':'HOME',
            'Home':'HOME','Food':'Food','Family':'Family','Login':'Login'}))

class FamilyHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/family.html')
    	self.response.write(template.render({'title': 'FAMILY','page':'Family',
            'Home':'Home','Food':'Food','Family':'FAMILY','Login':'Login'}))


class FoodHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/food.html')
    	self.response.write(template.render({'title':'FOOD','page':'Food',
            'Home':'Home','Food':'FOOD','Family':'Family','Login':'Login'}))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/login.html')
        self.response.write(template.render({'title': 'LOGIN','page':'Login',
            'Home':'Home','Food':'Food','Family':'Family','Login':'LOGIN'}))
    def post(self):
        name=self.request.get('name')
        pw=self.request.get('pw')
        logging.info(name)
        logging.info(pw)
        if name=="Colleen" and pw=="pass":
            template = JINJA_ENVIRONMENT.get_template('templates/right.html')
            self.response.write(template.render({'title': 'LoggedIn'}))
        else:
            template = JINJA_ENVIRONMENT.get_template('templates/login.html')
            self.response.write(template.render({'title': 'Fail','error':'Wrong Credential! Try again!',
                'Home':'Home','Food':'Food','Family':'Family','Login':'LOGIN'}))


app = webapp2.WSGIApplication([
    ('/', IndexHandler),
    ('/index', IndexHandler),
    ('/family', FamilyHandler),
    ('/food', FoodHandler),
    ('/login', LoginHandler),
    ('/right', LoginHandler),
    ('/login.html', LoginHandler)
], debug=True)
