from flask import Flask

from google.appengine.api import urlfetch
from lxml import html

from google.appengine.api import mail

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/check')
def check_logistik():
    url = "http://www.logistik24.ee"
    result = urlfetch.fetch(url,
                            follow_redirects=False,
                            deadline=10)
    if result.status_code == 200:
        # page = str(result.content)
        # tree = html.fromstring(page)
        #
        # title = tree.xpath('/html/body/div[1]')
        # test_div = title[0].get('ng-include')
        # print test_div
        # if test_div == 'components/navbar/navbar.html':
        #     print 'OK'
        # if test_div == 'components/navbar/navbar.html':
        mail.send_mail(sender="checker@logistik-pinger.appspotmail.com",
                       to="dmitribrach@gmail.com",
                       subject="logistik24.ee is online",
                       body="""
                            logistik24.ee is online
                            """)
        return 'OK'

    # TODO send email
    mail.send_mail(sender="checker@logistik-pinger.appspotmail.com",
                   to="dmitribrach@gmail.com",
                   subject="logistik24.ee is offline",
                   body="""
                        logistik24.ee is offline
                        """)
    return 'Error'


if __name__ == '__main__':
    app.run()
