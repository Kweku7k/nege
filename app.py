from flask import Flask,redirect,url_for,render_template,request, flash
from forms import RegistrationForm
import urllib.request, urllib.parse
import urllib

app=Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')


def send_sms(api_key,phone,message,sender_id):
    params = {"key":api_key,"to":phone,"msg":message,"sender_id":sender_id}
    url = 'https://apps.mnotify.net/smsapi?'+ urllib.parse.urlencode(params)
    content = urllib.request.urlopen(url).read()
    print (content)
    print (url)

@app.route('/form', methods=['GET','POST'])
def form():
    form = RegistrationForm()
    if form.validate_on_submit():
        print('Lezz geauxxx')
        flash(f'Your registration was successful. Please check your messages ', 'success')
        api_key = "aniXLCfDJ2S0F1joBHuM0FcmH" #Remember to put your own API Key here
        phone = "0545977791" #SMS recepient"s phone number
        message = "You have recieve a new registration from Nana Kweku."
        sender_id = "Basilissa" #11 Characters maximum
        send_sms(api_key,phone,message,sender_id)
        return redirect(url_for('home'))
    return render_template('register.html', form=form )
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(debug=True)