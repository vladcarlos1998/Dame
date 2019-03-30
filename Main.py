from obiecte.Dama import dama
from Repository.RepoDame import repo_dame
from Service.ServiceDame import ser_dame
from UI.UIDame import UI_dame

repo = repo_dame()
ser = ser_dame(repo)
ui = UI_dame(ser)
ui.run()