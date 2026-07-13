# here are all the curernt apps managed
from src import class_manager
from src.apps_list import notes
from src.apps_list import calculator

################################################################################
## . App options:
################################################################################
APP_ID = 1
APP_NAME = 2
NOTE_ID = 1
CALC_ID = 2

################################################################################
## . here is notes and calculator:
################################################################################

notes_app = notes.notes_app

calculator_app = calculator.calculator_app

APPS = {
    1: notes_app,
    2: calculator_app
}

################################################################################

def list_apps(option):
    # make this count apps
    #for loop through files inside src/apps
    app_list = [] 

    if option == APP_ID:
        app_list.append(notes_app.id)
        app_list.append(calculator_app.id)
    elif option == APP_NAME:
        app_list.append(notes_app.name)
        app_list.append(calculator_app.name)
    
    return app_list

def get_app(app_id):
    # search id list then return app
    if app_id == 1:
        return notes_app
    if app_id == 2:
        return calculator_app
    
def run_app(app_id, state):
    app = APPS.get(app_id)

    if not app:
        print("App not found")
        return
    
    app.run(state)