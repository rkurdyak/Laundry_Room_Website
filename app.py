from flask import Flask, render_template, request, redirect, url_for
import sqlite3  # Database setup for simplicity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# To handle new service requests
@app.route('/new_request', methods=['POST'])
def new_request():
    machine_id = request.form['machine_id']
    issue = request.form['issue']
    email = request.form['email']
    save_request(machine_id, issue, email)
    send_email_notification(machine_id, issue, email)
    return redirect(url_for('index'))

# To view historical requests
@app.route('/requests')
def view_requests():
    conn = sqlite3.connect('laundry.db')
    c = conn.cursor()
    c.execute("SELECT * FROM requests")
    all_requests = c.fetchall()
    conn.close()
    return render_template('view_requests.html', requests=all_requests)

# Function to save request in the database
def save_request(machine_id, issue, email):
    conn = sqlite3.connect('laundry.db')
    c = conn.cursor()
    c.execute("INSERT INTO requests (machine_id, issue, email) VALUES (?, ?, ?)", (machine_id, issue, email))
    conn.commit()
    conn.close()

# Dummy email sender function
def send_email_notification(machine_id, issue, email):
    print(f"Sending email to company about machine {machine_id} - issue: {issue}")
    # Add actual email sending logic here

if __name__ == '__main__':
    app.run(debug=True)
