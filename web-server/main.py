import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Hola soy una página</h1>
        <p>Soy un parrafo</p>
        <p>Vamos a ver si se sincroniza el cambio</p>
        <p>Otro cambio</p>
    """

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()