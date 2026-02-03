from flask import Flask,render_template, request
from weather import get_weather_data
from waitress import serve  

app = Flask(__name__)

@app.route('/')
@app.route('/index')



def index():
    return render_template('index.html', title='Weather App')

@app.route('/weather')
def get_weather():
    city = request.args.get('city', 'New York') 
    # Default to New York if no city is provided
    if not bool(city.strip()):
        city = "New York"
    weather_data = get_weather_data(city)

    #City is not found in the API
    if weather_data.get("cod") != 200:
        return render_template('city-not-found.html')
            
    return render_template (
        "weather.html", 
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"    
    )


if __name__ == '__main__':
    #print("Starting Waitress server on http://127.0.0.1:8000", flush=True)
    serve(app, host="0.0.0.0", port=8000)
    #app.run(host='127.0.0.1', port=8000, debug=True)