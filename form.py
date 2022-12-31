import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        student_first_name = request.form['student_first_name']
        student_last_name = request.form['student_last_name']
        student_class = request.form['student_class']
        student_email = request.form['student_email']
        student_presence = request.form['student_presence']
        guest = request.form['guest']
        guest_first_name = request.form['guest_first_name']
        guest_last_name = request.form['guest_last_name']

        print(f"Hello {student_first_name} {student_last_name}, from {student_class}. Your email address is: {student_email}")
        
     
        if student_presence == "Yes":
            if request.form.get('guest_first_name'):
                guest_first_name = request.form['guest_first_name']
                guest_last_name = request.form['guest_last_name']
    
                print(f"It's great that you're coming! Your guest is {guest_first_name} {guest_last_name}")
        
            else:
                print("It's great that you're coming! You have no guest for the moment.")
            
        
        else:
            print("Too bad... We'll see you another time, then!")
                
     
        if student_presence == "Yes":
            if request.form.get('guest_first_name'):
                print("The total amount of your order is (25€/pp):", 2*25 , "€")
            else:
                print("The total amount of your order is (25€/pp):", 1*25, "€")
        else:
            print("You do not need to make any payment.")
        
        print("Thank you for answering this form.")
        
        
        
        connection = mysql.connector.connect(
            host="cpd3",
            user="chrichri156",
            password="PassWord123",
            database="Event102"
        )    
    
        cursor = connection.cursor()

    
        sql = "INSERT INTO Attendees_List (student_first_name, student_last_name, student_class, student_email, student_presence, guest_first_name, guest_last_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (student_first_name, student_last_name, student_class, student_email, student_presence, guest_first_name, guest_last_name)
        cursor.execute(sql, values)

    
        connection.commit()
    

        cursor.close()
        connection.close()
        
        return render_template('success.html')
    
    
    
    else:
        return render_template('index.html')
