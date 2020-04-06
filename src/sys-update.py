import app
import sys
import requests

app = app.App('sys-update', version='0.1.a', desc= 'Releax OS Update Manager')

app.addAuthor('Pratyush Ratan', email='ratanpratyush@releax.in')

@app.args('check','[release]','check latest release')
def check_updates(*args):
    release = args[0].value_of('release', 'stable')
    mirror = args[0].value_of('mirror', 'http://127.0.0.1:5000/')
    url = "%s/check/%s" %  (mirror,release)
    try:
        resp = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        print("unable to connect to internet")
        
    print(resp.json())

app.run(sys.argv)
