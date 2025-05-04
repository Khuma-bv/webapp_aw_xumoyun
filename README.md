# Final Project: Full Web Application Deployment on AWS

## Student: Xumoyun Bolikulov

### ✅ Project Structure
- **Backend:** Python Flask App (EC2)
- **Database:** PostgreSQL on Amazon RDS
- **Static Site Hosting:** Amazon S3

### 🔗 Live Links
- **Books App (EC2):** http://3.35.19.94:5000/books
- **Static Homepage (S3):** http://2t-xumoyun.s3-website.ap-northeast-2.amazonaws.com

### 📁 Contents
- `app.py`: Flask application with Add/Delete
- `books.html`: HTML Template
- `README.md`: This file

### ⚙️ How to Run
1. Launch EC2, RDS, and S3 as described.
2. Activate Python venv and install requirements.
3. Run the Flask app: `python3 app.py`
4. Open EC2 IP in browser: `/books`
5. Use S3 public link for static page.