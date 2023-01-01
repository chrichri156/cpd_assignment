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
        total_amount = 0

        print(f"Hello {student_first_name} {student_last_name}, from {student_class}. Your email address is: {student_email}")
        
     
        if student_presence == "Yes":
            if request.form.get('guest_first_name') and request.form.get('guest_last_name'):
                guest_first_name = request.form['guest_first_name']
                guest_last_name = request.form['guest_last_name']
            
                print(f"It's great that you're coming! Your guest is {guest_first_name} {guest_last_name}")
        
            elif request.form.get('guest_first_name'):
                return "Error: Please provide a last name for your guest."
            
            else:
                print("It's great that you're coming! You have no guest for the moment.")
            
        
        else:
            print("Too bad... We'll see you another time, then!")
                
     
        if student_presence == "Yes":
            if request.form.get('guest_first_name') and request.form.get('guest_last_name'):
                total_amount = 2 * 25
            else:
                total_amount = 1 * 25
        
        else:
            total_amount = 0
        
        print("Thank you for answering this form.")
        
        
        
        connection = mysql.connector.connect(
            host="cpd3",
            user="chrichri156",
            password="PassWord123",
            database="Event102",
            use_sudo=True,
            sudo_user="root"
        )    
    
        cursor = connection.cursor()

    
        sql = "INSERT INTO attendees_list (student_first_name, student_last_name, student_class, student_email, student_presence, guest_first_name, guest_last_name, total_amount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (student_first_name, student_last_name, student_class, student_email, student_presence, guest_first_name, guest_last_name, total_amount)
        cursor.execute(sql, values)

    
        connection.commit()
    

        cursor.close()
        connection.close()
        
        return render_template('success.html', total_amount = total_amount)
    
    
    
    else:
        return render_template('index.html')
