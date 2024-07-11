from flask import Flask, render_template


app = Flask(__name__)

my_resume = {
    'name': 'Dalton K Hughes',
    'phone_num': ['(229) 231-2567', 'fa-phone'],
    'email': ['dhughes3223@gmail.com', 'fa-envelope'],
    'links': [['https://github.com/Dalton-K-Hughes', 'fa-github'], ['https://www.linkedin.com/in/dhughes3223/', 'fa-linkedin']],
    'projects': [
        {'name': 'Student Behavior Tracking System', 
         'description': [
            'Developed a Student Behavior Tracking System using Python, Django, and the Google Sheets API.',
            'Enabled students to access their behavior records and monitor progress through a user-friendly interface.',
            'Implemented real-time synchronization of behavior data with Google Sheets for accuracy and accessibility.',
            'Provided educators with customizable reporting tools to analyze behavior patterns and identify intervention opportunities',
            'Cultivated a culture of accountability and collaboration within the school community, fostering positive behavior reinforcement.']},
        {'name': 'Real Estate Eye', 
         'description': [
             'Developed Real Estate Eye Android application using Kotlin and Jetpack Compose',
             'Integrated OpenCV for advanced photo matching capabilities to identify listed properties.',
             'Created a custom API with Java and Spring for seamless communication with online databases.',
             'Streamlined the house-hunting process by providing users with accurate listing information through innovative image recognition technology.',
             ]},
        {'name': '', 
         'description': [
             
         ]}
    ]


}

@app.route('/')
def index():
    return render_template('index.html', template_resume = my_resume)