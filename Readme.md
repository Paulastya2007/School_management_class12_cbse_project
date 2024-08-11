This Project is made in a container environment

To start the container with SQL installed run this command
`docker-compose up -d`

Service name: `mysql`
Root Password: `my-secret-pw`



*For use in local machine use ur password*
*Make a Python Virtual Environment for this project*

Run: `python3 -m venv myenv`


To start the existing env
    
    Linux 
        `source myenv/bin/activate`
    
    Windows
        `myenv\Scripts\activate`


Install mysql connector 
        `pip install mysql-connector-python`


_Modify this line according to ur database and password and username_
most of the things should work out-of-the-box
default here is: `my-secret-pw`

        `db = mysql.connector.connect(user='root', password=<Password>, host='localhost',database='mysql')`
