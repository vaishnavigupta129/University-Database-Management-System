from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration - Update these with your MySQL details!
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root@123', 
    'database': 'university'
}

@app.route('/')
def index():
    # This renders your HTML form
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # 1. Get data from the HTML form
    s_id = request.form['student_id']
    s_name = request.form['student_name']
    d_name = request.form['dept_name']
    t_cred = request.form['tot_cred']

    try:
        # 2. Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 3. Execute the Insert query
        query = "INSERT INTO student (ID, name, dept_name, tot_cred) VALUES (%s, %s, %s, %s)"
        values = (s_id, s_name, d_name, t_cred)
        
        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
        return f"<h1>Success!</h1><p>Student {s_name} added to the database.</p><a href='/'>Go Back</a>"

    except mysql.connector.Error as err:
        return f"<h1>Error</h1><p>{err}</p><a href='/'>Try Again</a>"

if __name__ == '__main__':
    app.run(debug=True)