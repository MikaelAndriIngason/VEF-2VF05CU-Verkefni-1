from bottle import route, run

@route('/')
def hello():
    return "Halló heimur", '''
        <hr>
        <a href="/page/1">Sida 1</a><br>
        <a href="/page/2">Sida 2</a><br>
        <a href="/page/3">Sida 3</a>
    '''

@route('/page/<numer>')
def sida(numer=1):
    return "Síða ", numer, '''
        <hr>
        <a href="/">Index</a>
    '''

run(host='localhost', port=8080, debug=True)
