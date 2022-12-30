import mysql.connector

repeat_form = "Yes"
while repeat_form == "Yes":
    firstNameStudent = input ("Insert your first name:")
    lastNameStudent = input ("Insert your last name:")
    classStudent = input ("Insert your class:")
    email = input ("Insert your email address:")

    print(f"Hello {firstNameStudent} {lastNameStudent}, from {classStudent}. Your email address is: {email}")


    change_info = input ("Do you want to change those informations (Yes/No) ? ")
    
    if change_info == "Yes":
        continue
    elif change_info == "No":
        break
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

    repeat_form = "Yes"
    while repeat_form == "Yes":
    
        presence = input ("Will you be present at the Prom Ball on the 28th of June 2023? (Yes/No)") 
    
        if presence == "Yes":
            guest = input ("Will you be accompanied (maximum 1 guest) (Yes/No) ? ")
        
            if guest == "Yes":
                guest_firstname = input ("If yes, insert your guest’s first name:")
                guest_lastname = input ("If yes, insert your guest’s last name:")
        
                print(f"It's great that you're coming! Your guest is {firstNameGuest} {lastNameGuest}")
            
            else:
                print("It's great that you're coming! You have no guest for the moment.")
                
            
        elif presence == "No":
            print("Too bad... We'll see you another time, then!")
        
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
        
        change_info = input("Do you want to change those informations (Yes/No) ? ")
        if change_info == "Yes":
            continue
        
        elif change_info == "No":
            break
        
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")



    if presence == "Yes"
        if guest == "Yes":
         print("The total amount of your order is (25€/pp):", 2*25 , "€")
        
    elif presence == "Yes" and guest == "No":
        print("The total amount of your order is (25€/pp):", 1*25, "€")
    
    again3 = input ("Do you want to change those informations (Yes/No) ? ")

print("Thank you for answering this formular.")


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        firstNameStudent = request.form['first_name']
        lastNameStudent = request.form['last_name']
        classStudent = request.form['class']
        email = request.form['email']
        presence = request.form['presence']
        firstNameGuest = request.form['guest_first_name']
        lastNameGuest = request.form['guest_last_name']

        
        
        connection = mysql.connector.connect(
            host="cpd3",
            user="chrichri156",
            password="PassWord123",
            database="Event102"
        )    
    
        cursor = connection.cursor()

    
        sql = "INSERT INTO Attendees_List (first_name, last_name, class, email, presence, guest_first_name, guest_last_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (firstNameStudent, lastNameStudent, classStudent, email, presence, firstNameGuest, lastNameGuest)
        cursor.execute(sql, values)

    
        connection.commit()
    

        cursor.close()
        connection.close()
        
        return render_template('success.html')
    
    
    
    else:
        return render_template('index.html')
