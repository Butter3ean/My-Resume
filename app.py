from flask import Flask, render_template


app = Flask(__name__)

my_resume = {
    'name': 'Dalton K Hughes',
    'phone_num': ['(229) 231-2567', 'fa-phone'],
    'email': ['dhughes3223@gmail.com', 'fa-envelope'],
    'links': [['https://github.com/Dalton-K-Hughes', 'fa-github'], ['https://www.linkedin.com/in/dhughes3223/', 'fa-linkedin']],
    'skills': [
        {'languages': ['python', 'kotlin', 'java', 'html', 'css', 'javascript', 'c#']}, 
        {'frameworks': ['flask', 'jetpack compose', 'spring', 'react', 'django']}, 
        {'databases': ['postgreSQL', 'mongoDB', 'mySQL', 'sqlite']}],
    'projects': [
        {'name': 'Student Behavior Tracking System', 
         'description': [
            'Developed a Student Behavior Tracking System using Python, Flask, and the Google Sheets API.',
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
        {'name': 'Pokemon Card Collector', 
         'description': [
             'Developed a robust Pokemon card collector application using Kotlin within Android Studio.',
             'Designed intuitive user interfaces (UI) using XML for seamless navigation and enhanced user experience.',
             'Implemented Android Room for efficient local storage and management of Pokemon card data, ensuring offline functionality.',
             'Collaborated closely with a team member, conducting weekly meetings to track progress and resolve challenges.',
             'Integrated a RESTful API for real-time updates, enriching the app\'s features and expanding card collection capabilities.'
             
         ]}],
    'work experience': {
            'title': 'Computer Science Teacher',
            'location': 'Lee County Middle School East',
            'description': ['Instructed grades 6-8 in HTML/CSS, JavaScript, Python, and Physical Computing, fostering a dynamic learning environment to engage students in technology and computer science concepts.',
                            'Designed and delivered comprehensive lesson plans, incorporating innovative teaching methodologies to facilitate student understanding and retention.',
                            'Mentored and guided students in developing software projects, providing hands-on assistance and technical support throughout the development lifecycle.', 
                            'Collaborated with fellow educators to integrate technology into the curriculum, enhancing student learning outcomes and preparing them for future careers in technology.']
        }}


@app.route('/')
def index():
    return render_template('index.html', template_resume = my_resume)