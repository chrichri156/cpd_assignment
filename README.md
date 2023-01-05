<h1 align="center">ASSIGNMENT - 12/2022</h1>

<h3 align="center">B8IS131 - Cloud Platform Development - Paul Laird</h3>

<h3 align="center">Cloud POC deployment</h3>

<h3 align="center">10625302 JANSEN Christelle</h3>

***

### 1. Short background of the enterprise and their requirements for some IT service


*Love Is All* is a small Belgian company that manages a restaurant ("*Vertigo*") and a famous cocktail bar ("*Jalousy*") in Brussels. As they are part of the hotel, restaurant and catering sector, there is a significant need for accessing their data very quickly, in order not only to manage real-time orders, but also to manage their inventory, the orders to their suppliers, and their financial results and their profitability.

Although there is currently a lot of platforms that already help the management of such establishments, those companies still need "one" platform to centralise, in real time, all the others, or basically all the information.



### 2. Recommendations for migration of the service to the Cloud


This central system should be a cloud-based ERP platform (Enterprise Resource Planning), such as Oracle, SAP or Growzer (the one that I use during my internship in their company). Indeed, the characteristics of cloud-based ERP platforms are essential for an efficient support for the management of HoReCa businesses:

- **Integration:** In order to gather all the information in one place, they can be easily integrated with other systems, such as suppliers systems (to allow easy placement of orders, which can be for example automatically sent regarding the low stock of the product/ingredient).

- **Accessibility:** Restaurant's businesses often use the cloud-based ERP LightSpeed platform to manage orders (linking the service room to the bar and the kitchen, as well as the cash register). As mentioned above, cloud-based ERP platforms can be linked to others, so does Growzer with LightSpeed. Therefore, on the one hand, it allows the staff to use those platforms anywhere with an internet connection (in the kitchen, the basement, the service room...). On the other hand, the managing team also have access to the real-time information and results anywhere with an internet connection (in the office, in the building, at home...)

- **Costs saving:** If the ERP platform weren't cloud-based, the company would need to invest in expensive hardware and infrastructure to host it, or they would need some specific materials to install and use existing ERP platforms (like installation CDs, or special keys).
Besides, as everything is gathered real-time in one place, the managing team can easily use all the information to set up better strategies (for example, which meals are the most/least bought; what should be the price of this item, based on the production costs and the profit margin...), based on the platform's analysis.

- **Scalability:** As every business has a durability goal, they always want to evolve and to grow. However, when experiencing a growth, everything has to follow it, even IT resources. With cloud-based platforms, this can be done easily.

- **Operational intelligence:** Thanks to integration and real-time data about their operations (such as financial performance, inventory levels, and costs analysis), HoReCa companies are more able to make informed decisions, to set up efficient strategies and to respond more quickly to changes in their business environment, improving their overall efficiency and productivity.



Moreover, in terms of cloud computing offerings, HoReCa companies should turn to SaaS solutions (Software as a Service). This is the case with the ERP "*GROWZER*", that *Love Is All* uses. It is the closest solution to the users (the HoReCa company, the managers and the staff), as they don't have to install or maintain the software on their own computers or servers. They just pay a monthly or annual subscription fee for access.

However, from the cloud-based ERP platform, or if the HoReCa managers want to create their own platform, they should use a PaaS solution (Platform as a Service), such as Microsoft Azure or Google Cloud Platform.

> *Expert Network (to whom the GROWZER team reached out for developing the platform) chose an Microsoft Azure cloud-based solution that would check not only the most important boxes in terms of a wide palette of choices but would also provide solid ground for the support of modern platform architecture. Some core functionalities added include menu engineering, cloud-based purchase order system, centralised ordering, app responsiveness as well as stock management. The app was also designed to be operational on a tablet and to be responsive, meaning that it responds to input promptly, without leaving the users hanging.*

Wildstream (2022). *Expert Network - Growzer* Available from: https://wildstream.be/case/expert-network-growzer/ [accessed on 01 January 2023].


This choice for a PaaS solution allows the company to take advantage of the scalability and reliability of a cloud-based infrastructure, while still being able to customise their ERP platform to meet their specific business needs.



Finally, only this last category of client (cloud-based ERP platform builders, or HoReCa managers that want to create their own ERP platform) should use a continuous development strategy, as it refers to a software development approach, that most of the time doesn't concern the HoReCa managers/staff. Continuous development consists of continuously developing and delivering software updates, based on the client/user feedback with identified issues that the development can fix. It also allows organisations to respond more quickly to changing business needs and market conditions.
As for the other category, they should turn to SaaS platforms that use a continuous development strategy, so that they can easily notify issues and help developers to target client, businesses and market expectations.



### 3. Documentation of Proof-of-Concept Solution


For a student event, I wanted to create a Web App to display a form (like a Google form) to be filled in by the students (with the student details, whether they would be present and have a guest or not, and with the guest details if applicable). If well filled in, the Web App should return the total amount of the order, knowing that 1 entry = 25€.

Form example (from a regular user perspective):

    Insert your first name:
    Insert your last name:
    Insert your class:
    Insert your email address:

    Will you be present at the Prom Ball on the 28th of June 2023?
    Will you be accompanied (maximum 1 guest)?
    If yes, insert your guest’s first name:
    If yes, insert your guest’s last name:

    The total amount of the order is:


The answers should be then stored in a MySQL database table.

Additionaly, I wanted to display, when entering the Web App, a log-in connection possibility for the event organisers, so that they could see the answers in a table (like an Excel table) and modify it.

The table should look like this:

| student_first_name | student_last_name | student_class | student_email | student_presence | guest | guest_first_name | guest_last_name | total_amount |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Christelle | Jansen | 6T8 | christelle.jansen@hotmail.fr | 1 | 1 | Juliette | Chardon | 50€ |

The admin log-in script:

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    while username != "chrichri156" or password != "PassWord123":
        print("Either you have made a mistake in your username and/or password, or you do not have access to the admin account.")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

    print(f"Welcome {username}. You are well logged in to the admin account.")


However, as I struggle with the first goal, I didn't continue this improvement.


In order to display the form on the Web App, I created a Virtual Machine with Microsoft Azure ("cpd3" ; "https://cpd3.westeurope.cloudapp.azure.com/"). I connected my VM to my Visual Studio Code terminal using SSH, then I created a Docker repository to host the containers, that I connected with the VM.

I first began with the form.py file, searching for the right way of executing the form and storing the answers in the MySQL table "attendees_list", in the database "Event102", in the resource group "cpd_assignment". I first wrote a simple version of a Python script for the form:


    again3 = "Yes"
    while again3 == "Yes":


        again1 = "Yes"
        while again1 == "Yes":
            firstNameStudent = input ("Insert your first name:")
            lastNameStudent = input ("Insert your last name:")
            classStudent = input ("Insert your class:")
            email = input ("Insert your email address:")

            print(f"Hello {firstNameStudent} {lastNameStudent}, from {classStudent}. Your email address is: {email}")


            again1 = input ("Do you want to change those informations (Yes/No) ? ")
    

        again2 = "Yes"
        while again2 == "Yes":
    
            presence = input ("Will you be present at the Prom Ball on the 28th of June 2023? (Yes/No)") 
    
            if presence == "Yes":
    
                guest = input ("Will you be accompanied (maximum 1 guest) (Yes/No) ? ")
        
                if guest == "Yes":
    
                    firstNameGuest = input ("If yes, insert your guest’s first name:")
                    lastNameGuest = input ("If yes, insert your guest’s last name:")
        
                    print(f"It's great that you're coming! Your guest is {firstNameGuest} {lastNameGuest}")
            
                else:
                    print("It's great that you're coming! You have no guest for the moment.")
                
            
            else:
                print("Too bad... We'll see you another time, then!")
        
            again2 = input ("Do you want to change those informations (Yes/No) ? ")



        if presence == "Yes" and guest == "Yes":
             print("The total amount of your order is (25€/pp):", 2*25 , "€")
        
        elif presence == "Yes" and guest == "No":
            print("The total amount of your order is (25€/pp):", 1*25, "€")
    
        again3 = input ("Do you want to change those informations (Yes/No) ? ")

    print("Thank you for answering this formular.")


In the meantime, I installed all the apps and dependencies necessary for my purposes, like Flask, pip, mysql,...
I also created my user credentials and the table in the MySQL database, using the following command:

    CREATE USER 'chrichri156'@'cpd3' IDENTIFIED BY 'PassWord123';
    GRANT ALL PRIVILEGES ON *.* TO 'chrichri156'@'cpd3';
    CREATE DATABASE Event102;
    GRANT ALL PRIVILEGES ON Event102.* TO 'chrichri156'@'cpd3';
    FLUSH PRIVILEGES;

    CREATE TABLE attendees_list (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_first_name VARCHAR(255) NOT NULL,
        student_last_name VARCHAR(255) NOT NULL,
        student_class VARCHAR(255) NOT NULL,
        student_email VARCHAR(255) NOT NULL,
        student_presence VARCHAR(255) NOT NULL,
        guest_first_name VARCHAR(255),
        guest_last_name VARCHAR(255),
        total_amount INT
    );


I then created the index.html file, which consists of the structure of the Web App (add a new field to fill in with the name, add two buttons for "Yes" and "No" answers...). The related file index_style.css hosts the style of the Web App page "index.html" (which colour, which alignment...).
The success.html file was then created, for returning a thanking message and information for the payment. The related file success_style.css file hosts the style of the Web App page "success.html" (which colour, which alignment...).

I finally created the Dockerfile, which hosts the Docker container and the Docker images. It explains the system what to do: which programme to install, which file to search and where, what needs to be done, etc.).

However, after improving little by little all my files, I still can't run the Web App on http://cpd3.westeurope.cloudapp.azure.com

After running, in my terminal, the command: docker build -t cpd_assignment .
I get this:

But when I run this: docker run -p 80:3000 cpd_assignment
Then nothing happened, and I can write something again. And when I check with the "docker ps" command, there is no container at all, actually.


    chrichri156@cpd3:~/cpd_assignment$ git pull
    Already up to date.
    chrichri156@cpd3:~/cpd_assignment$ docker build -t cpd_assignment .
    Sending build context to Docker daemon  526.3kB
    Step 1/8 : FROM python:3.8-slim
     ---> 61afbf515f15
    Step 2/8 : RUN python -m pip install pip==22.3.1 &&   pip install flask &&   pip install mysql-connector-python
     ---> Using cache
     ---> ea5708a7595a
    Step 3/8 : WORKDIR /cpd_assignment
     ---> Using cache
     ---> f3a60e5b4e8a
    Step 4/8 : COPY . /cpd_assignment
     ---> 7f92b0ff6df3
    Step 5/8 : CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
     ---> Running in 3c2ae7abb78e
    Removing intermediate container 3c2ae7abb78e
     ---> 9a8aac8c2a5d
    Step 6/8 : EXPOSE 3000
     ---> Running in e88768a39192
    Removing intermediate container e88768a39192
     ---> 3b3756ebd609
    Step 7/8 : ENTRYPOINT ["python", "form.py"]
     ---> Running in f12fdfec0b8c
    Removing intermediate container f12fdfec0b8c
     ---> ca746d8416d4
    Step 8/8 : HEALTHCHECK --interval=30s --timeout=5s CMD ["curl", "-f", "http://cpd3.westeurope.cloudapp.azure.com:80"]
     ---> Running in ecdcbf2a1c23
    Removing intermediate container ecdcbf2a1c23
     ---> 116e8f68fcb6
    Successfully built 116e8f68fcb6
    Successfully tagged cpd_assignment:latest
    chrichri156@cpd3:~/cpd_assignment$ docker run -p 80:3000 cpd_assignment
    chrichri156@cpd3:~/cpd_assignment$
    chrichri156@cpd3:~/cpd_assignment$ sudo systemctl stop apache2
    chrichri156@cpd3:~/cpd_assignment$ docker run -d -p 80:3000 cpd_assignment
    4e5a4b6aa5d946b42d15c11f5aebf9712b019ca88ce417ccb7afdc05d1e24392
    chrichri156@cpd3:~/cpd_assignment$ docker ps
    CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
    chrichri156@cpd3:~/cpd_assignment$
    
I tried multiple things to correct this issue, but I don't understand why it is not running properly. I only know it has something to do with the Dockerfile instructions, and maybe the form.py file. Somehow, the Docker container is not built properly, even if the "docker build" command returned successfully.

**UPDATE:**

I found a way to force the building of the Docker container. Now, the first page is well being displayed (the form to fill in), but when clicking on submitting, it leads to an error page.

The problem is that I can't enter MySQL using the command I want in the terminal:
    
    mysql -h cpd3 -u chrichri156 -p
    
I get an error message:
    
    ERROR 2003 (HY000): Can't connect to MySQL server on 'cpd3:3306' (111)
    
I succeed this step using either the command:
    
    sudo mysql

or

    mysql -h localhost -u chrichri156 -p

However, the same error appears when submitting the form (thus during the step where MySQL is open and where the answers should be stored in the database table).

I checked for various solutions, such as verifying the port, the hostname, the password, the privileges, the firewall or the port allowed in Azure, yet (after some changes), I can't find the solution or understand how I could do.

![Capture d’écran 2023-01-02 023856](https://user-images.githubusercontent.com/114661244/210190238-8d08f25b-6644-42c2-b6cf-1ef4c09663e3.png)
![Capture d’écran 2023-01-02 024106](https://user-images.githubusercontent.com/114661244/210190244-2039b497-7eb8-4777-9b29-90bc0a4c907a.png)
![Capture d’écran 2023-01-02 024126](https://user-images.githubusercontent.com/114661244/210190249-5b661e62-dc12-466c-bea5-77ca78132e5e.png)


**UPDATE 04/01/2023:** After submitting my assignment, I used a joker and asked a friend to help me find the little problem with the MySQL connection, so now the webpage is actually working!

He just changed the bind-address from **"127.0.0.1" to "0.0.0.0"** in the nano environment of MySQL:

    sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
    
He also added the user "chrichri156" with the hostname "%" and the password "PassWord123", and granted all the privileges:

    CREATE USER 'chrichri156'@'%' IDENTIFIED BY 'PassWord123';
    GRANT SELECT, INSERT, DELETE ON *.* TO 'chrichri156'@'%';
    GRANT ALL PRIVILEGES ON *.* TO 'chrichri156'@'%';
    
Therefore, the connection to the database is well working, and the success.html webpage is well displayed when the form is submitted.

With a guest:
![Capture d’écran 2023-01-05 114534](https://user-images.githubusercontent.com/114661244/210762890-e23c0781-5ca0-4f19-99e6-4087e929ba32.png)
![Capture d’écran 2023-01-05 114826](https://user-images.githubusercontent.com/114661244/210762901-0a0e2c4d-ec72-4a9a-9e2b-650bdc0091ef.png)

Without a guest:
![Capture d’écran 2023-01-05 114834](https://user-images.githubusercontent.com/114661244/210762928-4d2588ae-0559-4b2c-a2e0-61f75d41012e.png)
![Capture d’écran 2023-01-05 114840](https://user-images.githubusercontent.com/114661244/210762949-8c7fb23a-243f-45db-9083-5df55f145bbb.png)

Not participating:
![Capture d’écran 2023-01-05 114847](https://user-images.githubusercontent.com/114661244/210762963-89bae0b6-773b-44d3-a42d-820c22bccb25.png)
![Capture d’écran 2023-01-05 114854](https://user-images.githubusercontent.com/114661244/210762980-aff2e513-c66e-4159-9f39-ceb1e608f1b0.png)

