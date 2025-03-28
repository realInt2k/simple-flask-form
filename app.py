from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_title = request.form.get('job_title', '').strip()
        city_name = request.form.get('city_name', '').strip()
        return f"Job Title: {job_title}, City Name: {city_name}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(port=5001, debug=True)
