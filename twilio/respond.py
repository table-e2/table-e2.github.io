from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import subprocess
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body[0:7] == 'Newhigh':
        num = body[7:]
        result = ''
        with open('currentData.txt') as f:
            for i in range(int(num)):
                result += str(i + 1)
                result += '. '
                result += f.readline()
        # resp.message(result.stdout.decode('utf-8'))
        resp.message(result)
        return str(resp)
        
    if body[0:6] == 'Newlow':
        num = body[6:]
        result = subprocess.run(['tail','-n',num,'currentData.txt'], stdout=subprocess.PIPE)
        resp.message(result.stdout.decode('utf-8'))
        return str(resp)
    if body[0:4] == 'High':
        num = body[4:]
        num = '-' + num
        result = subprocess.run(['head',str(num),'AllBuildings.txt'], stdout=subprocess.PIPE)
        resp.message(result.stdout.decode('utf-8'))
        return str(resp)
    if body[0:3] == 'Low':
        num = body[3:]
        result = subprocess.run(['tail','-n',num,'AllBuildings.txt'], stdout=subprocess.PIPE)
        resp.message(result.stdout.decode('utf-8'))
        return str(resp)
    if body == 'Hourly':
        result = subprocess.run(['cat','ByHour.txt'], stdout=subprocess.PIPE)
    elif body == 'Weekday':
        result = subprocess.run(['cat','DaysOfWeek.txt'], stdout=subprocess.PIPE)
       # resp.message(fortune)
    elif body == '10minute':
        result = subprocess.run(['cat','data/PerTenMinutes.txt'], stdout=subprocess.PIPE)
    else:
        resp.message("June 2018 - Feb 2019 Totals\n\nCommands:\n(# is any number between 1 and 50)\nNewhigh# - Highest Past 10 Minutes\nNewlow# - Lowest Past 10 Minutes\n\nBelow are cumulative annual figs:\nHigh# - Highest of Year\nLow# - Lowest of Year\n\nCampuswide Figures:\n10minute - Ten Minute Intervals\nHourly - 1 Hour Intervals\nWeekday - By Day of the Week\n")
        return str(resp)
    resp.message(result.stdout.decode('utf-8'))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
