from flask import Flask, render_template
app = Flask(__name__)
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

print("calling getactivelist function")
print(getActiveList())

@app.route("/")
def return_file():
  return render_template('index.html',len=len(getActiveList()),active=getActiveList())

if __name__ == "__main__":
  app.run(debug=True)