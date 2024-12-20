from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(200) , nullable = False)
    desc = db.Column(db.String(500) , nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        print(title, desc)
        todo = Todo(title =title, desc =desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    print(type(allTodo))
    return  render_template('index.html',alltodo = allTodo)

@app.route('/show')
def product():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is product page!'

@app.route('/update/<int:sno>',methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST' :
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno = sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno = sno).first()
    return render_template('update.html',todo = todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True , port= 8000)
# @app.route('/make_db')
# def make_db():
#     db.create_all()
#     return ""



"""
- Programming exercises
- Programming projects
- Mathematics
- Englis
    - h


---------
Leetcode                     |                Website
(Python, Algorithm)          |     HTML, CSS, Javascript, SQL    
- python (course mitocw)     |      FastAPI       (Fastapi, html, css, javascript, sql => todo)         
- Algorithms (mitocw)        |              Online  

1. Leetcode
    - 
2. python (course mitocw) 1 video + exercises
    - Download
3. Fastapi Basic website (Hi, Deepak)


"""
# a = input("Give a number")

# try:
#     int(a)
# except:
#     raise UserTooDumbError("")
