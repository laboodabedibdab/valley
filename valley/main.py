import eel

eel.init("web")


@eel.expose
def get_inf(nick, password, tel):
    print(nick, password, tel)


eel.start("main.html", mode="chrome", size=(700, 400))
