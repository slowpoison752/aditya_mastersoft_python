from basicProject import app,db
import credentials
from flask  import render_template, redirect,request,url_for,flash,abort
from flask_login import login_user,login_required,logout_user,current_user
from basicProject.models import User
from basicProject.forms import LoginForm,Registration
from wit import Wit
access_token = "7LHLBTGCSZBBZPNH66R5WZV7MMTWJFWN"
bot = Wit(access_token = access_token)


#resp = client.message(message)
#print(resp)

@app.route('/')
def home():
    #flash("Please login or register!")
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome():
    name = current_user.username
    print(name)
    return render_template('welcome.html', name = name)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('User logged out')
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        
        #if (user is None):
        #    flash("Please provide correct log in credentials or register!")        
        if not(user.check_password(form.password.data)and user is not None):
            flash("Please provide correct log in credentials or register!")
        elif user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully!')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('welcome')
            return redirect(next)


    return render_template('login.html', form=form)


@app.route('/register', methods = ['GET', 'Post'])
def register():
    form = Registration()

    if form.validate_on_submit():
        user = User(email=form.email.data,
        username=form.username.data,
        password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Thank you for registering")
        return redirect(url_for('login'))
    return render_template('register.html', form= form)

if __name__ =='__main__':
    app.run(debug=True)

