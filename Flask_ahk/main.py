from flask import Flask, render_template
app = Flask(__name__)
from ahk import AHK
from ahk.window import Window
ahk = AHK()
win = list(ahk.windows())
active = []
for w in win:
    a=w.title
    a=a.decode('utf-8')
    active.append(a)


@app.route("/")
def return_file():
  return render_template('index.html',len = len(active),active=active)

if __name__ == "__main__":
  app.run(use_reloader = True, debug=True)