import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') #decorator
def get_list():
    return [1,2,3,4]

@app.get('/contac', response_class=HTMLResponse) #decorator with output in html
def get_list():
    return """
        <h1>Hoy soy un Titular</h1>
        <p>y Yo soy un parrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()