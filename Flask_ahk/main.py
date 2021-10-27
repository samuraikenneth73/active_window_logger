from flask import Flask, render_template
from ahk import AHK
from ahk.window import Window

def getActiveList():
  ahk = AHK()
  win = list(ahk.windows())
  active = []
  for w in win:
      a=w.title
      if a:
        a=a.decode('utf-8')
        active.append(a)
  return active


if __name__ == "__main__":
  app = Flask(__name__)
  
  @app.route("/")
  def return_file():
    print("calling getactivelist function")
    ar = getActiveList()
    return render_template('index.html',len=len(ar),active=ar)
  
  app.run()
