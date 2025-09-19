from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        name = request.form.get("name")
        room_no = int(request.form.get("room_no"))
        rent = int(request.form.get("rent"))
        food = int(request.form.get("food"))
        electricity_used = int(request.form.get("electricity_used"))
        units = int(request.form.get("units"))
        persons = int(request.form.get("persons"))

        electricity_bill = electricity_used * units
        monthly_bill = (rent + food + electricity_bill) // persons

        return f"""
        <html>
        <head>
            <style>
                body {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    color: #f0f0f0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    background: #3b3b98;
                    padding: 30px 40px;
                    border-radius: 12px;
                    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
                    width: 350px;
                    text-align: center;
                }}
                h2 {{
                    margin-bottom: 25px;
                    font-weight: 700;
                }}
                p {{
                    font-size: 18px;
                    margin: 15px 0;
                }}
                a.button {{
                    display: inline-block;
                    padding: 12px 24px;
                    margin-top: 20px;
                    background: linear-gradient(45deg, #f9a825, #ff6f00);
                    color: black;
                    font-weight: 700;
                    text-decoration: none;
                    border-radius: 8px;
                    transition: background 0.3s;
                }}
                a.button:hover {{
                    background: linear-gradient(45deg, #ff6f00, #f9a825);
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Monthly Rent Details</h2>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Room No:</strong> {room_no}</p>
                <p><strong>Monthly Bill:</strong> ₹{monthly_bill}</p>
                <a href="/" class="button">Calculate Again</a>
            </div>
        </body>
        </html>
        """

    # For GET request, show input form
    return """
    <html>
    <head>
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #3b3b98;
            padding: 40px 45px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
            width: 350px;
        }
        h2 {
            margin-bottom: 25px;
            font-weight: 700;
            text-align: center;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            font-size: 15px;
        }
        input[type=text], input[type=number] {
            width: 100%;
            padding: 10px 12px;
            margin-bottom: 20px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            outline: none;
        }
        input[type=number]::-webkit-inner-spin-button,
        input[type=number]::-webkit-outer-spin-button {
            -webkit-appearance: none;
            margin: 0;
        }
        button {
            width: 100%;
            padding: 14px 0;
            background: linear-gradient(45deg, #f9a825, #ff6f00);
            border: none;
            border-radius: 8px;
            color: black;
            font-weight: 700;
            font-size: 17px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: linear-gradient(45deg, #ff6f00, #f9a825);
        }
    </style>
    </head>
    <body>
    <div class="container">
        <h2>Rent Calculator</h2>
        <form method="POST" action="/">
            <label>Name:</label>
            <input type="text" name="name" required>

            <label>Room No:</label>
            <input type="number" name="room_no" required>

            <label>Rent:</label>
            <input type="number" name="rent" required>

            <label>Food:</label>
            <input type="number" name="food" required>

            <label>Electricity Used (units):</label>
            <input type="number" name="electricity_used" required>

            <label>Rate per Unit:</label>
            <input type="number" name="units" step="0.01" required>

            <label>Number of Persons:</label>
            <input type="number" name="persons" required>

            <button type="submit">Calculate</button>
        </form>
    </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
