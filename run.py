#!flask/bin/python
from app import app
import os
dport = int(os.environ.get('PORT'))
app.run(debug=True, host="0.0.0.0", port = dport)