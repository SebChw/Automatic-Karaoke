from flask import Flask, render_template, request

app = Flask(__name__)

# Define a list of instruments
instruments = ['Guitar', 'Vocal', "Drums", "Other"]  # Add more instruments as needed

@app.route('/')
def index():
    return render_template('index.html', instruments=instruments)

@app.route('/upload', methods=['POST'])
def upload():
    print(type(request))
    print(request)
    print(request.form)
    print(request.files)
    # Handle file upload and form submission here
    # Extract form data and process the uploaded file
    # Based on the selected options, perform the necessary actions
    
    return render_template('index.html', instruments=instruments, show_download=True)

if __name__ == '__main__':
    app.run(debug=True)