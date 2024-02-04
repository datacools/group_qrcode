from fastapi.templating import Jinja2Templates

def get_templates(directory:str='templates'):
    return Jinja2Templates(directory=directory)