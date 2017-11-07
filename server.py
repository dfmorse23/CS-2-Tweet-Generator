import os
from flask import Flask

the_app = Flask(__name__)

@the_app.route('/')
def hello_word():
    print("hellow world")

if __name__ == "__main__":
    # goes up to heroku server saved in the local enviornment
    port = int(os.environ.get('PORT', 5000))
    the_app.run(host='0.0.0.0', port=port)

#
# [[source]]
# url = "http://127.0.0.1:5000/"
# verify_ssl = true
#
# [packages]
# dj-database-url = "*"
# django = "*"
# gunicorn = "*"
# psycopg2 = "*"
# whitenoise = "*"
#
# [requires]
# python_version = "2.7.10"

# [requires]
# python_version = "3.6.2"
