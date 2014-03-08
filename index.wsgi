import os
import sys
import sae
import wsgi_app

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))
application = sae.create_wsgi_app(wsgi_app.application)