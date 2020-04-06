import app
import sys

app = app.App('sys-update', version='0.1.a', desc='System managment tool')

app.addAuthor('Manjeet Singh',email='itsmanjeet@releax.in')

@app.args('check','[release]','check latest release')
def check_updates(*args, **kargs):
    print('hello i am check updates')
    print(args[0].get_args())
    print(args[0].is_set('hello'))


app.run(sys.argv)