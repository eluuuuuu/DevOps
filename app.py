from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Change if you have a different MySQL username
app.config['MYSQL_PASSWORD'] = 'ComputingDP14!'  # Add your MySQL password if 
app.config['MYSQL_DB'] = 'crm'  # Your schema name

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])  # Hash password for security

        cur = mysql.connection.cursor()
        # Changed table name from users to crm_table
        cur.execute("INSERT INTO crm_table (username, email, password) VALUES (%s, %s, %s)",
                    (username, email, password))
        mysql.connection.commit()
        cur.close()
        
        return redirect('/success')  # Redirect to success page

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
