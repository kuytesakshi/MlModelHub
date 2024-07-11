from flask import Flask, render_template, requestimport pandas as pd
app = Flask(__name__)
df = None  # Global variable to store the DataFrame
@app.route("/")
def clean_data():    return render_template("dataclean.html")
@app.route("/success", methods=["POST"])
def data_uploaded():    global df  # Declare the global variable
    if request.method == "POST":
        result = []
        if 'csvFile' not in request.files:            mssg = "No file part"
            color = "red"            result = [mssg, color]
            return render_template("dataclean.html", result=result)
        file = request.files['csvFile']
        if file.filename == '':            mssg = "No selected file"
            color = "red"            result = [mssg, color]
            return render_template("dataclean.html", result=result)
        if file:            try:
                df = pd.read_csv(file)                color = "green"
                mssg = "The Data is uploaded successfully. Please select the Model Now."                result = [mssg, color]
            except Exception as e:                mssg = f"Error processing file: {e}"
                color = "red"                result = [mssg, color]
    return render_template("dataclean.html", result=result)
if name == "__main__":
    app.run(debug=True)    print(df)  # This will be executed after the server stops
