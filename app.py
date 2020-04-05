from flask import Flask , render_template , request
import requests

app =Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def weather():
 	return render_template('weather.html')

@app.route('/submit' , methods=['POST'])
def submit():
	if request.method=='POST':
		city =request.form['city']
		r=requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid=92fcf468b93ab42cb07e0b33456f2e66')
		json_object = r.json()
		temp_k =int(json_object['main']['temp'])
		temp_c=int(temp_k-273.15)

		
		return render_template('success.html' , city=city , temperature=temp_c)



if __name__ == '__main__':
 	app.run()