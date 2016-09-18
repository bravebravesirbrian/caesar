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
import cgi
from caesar import encrypt

page_header = """
<!DOCTYPE html>
<html>
<head>
</head>
<body>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    """Handles requests coming in to '/' (the root of the site)
    """

    def get(self):
    # a form for rotating letters
        rotate_form = """
        <form action="/" method="post">
            <label>
                I want to rotate
                <input type="text" name="text"/>
                by
                <input type="text" name="rotation"
                .
            </label>
            <input type="submit" value="Rotate"/>
        </form>
        """
        self.response.write(rotate_form)
    def post(self):

        new_text = str(self.request.get("text"))
        new_text = cgi.escape(new_text, quote=True)
        rotation_number = int(self.request.get("rotation"))
        response = encrypt(new_text, rotation_number)
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
