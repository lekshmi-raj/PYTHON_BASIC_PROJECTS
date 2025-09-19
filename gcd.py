from flask import Flask, request, render_template_string

app = Flask(__name__)

def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

HTML_FORM = """
<!doctype html>
<html>
<head>
  <title>GCD Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f7f9fc;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .container {
      background: white;
      padding: 30px 40px;
      border-radius: 10px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.1);
      width: 350px;
      text-align: center;
    }
    h2 {
      margin-bottom: 20px;
      color: #333;
    }
    input[type=number] {
      width: 100%;
      padding: 10px 15px;
      margin: 10px 0 20px 0;
      border-radius: 5px;
      border: 1px solid #ccc;
      box-sizing: border-box;
      font-size: 16px;
    }
    input[type=submit] {
      background-color: #007bff;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 5px;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.3s ease;
      width: 100%;
    }
    input[type=submit]:hover {
      background-color: #0056b3;
    }
    .result {
      margin-top: 20px;
      font-size: 20px;
      color: #28a745;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Find GCD of Two Numbers</h2>
    <form method="POST">
      <input type="number" name="num1" placeholder="Enter first number" required>
      <input type="number" name="num2" placeholder="Enter second number" required>
      <input type="submit" value="Calculate GCD">
    </form>
    {% if gcd is not none %}
      <div class="result">GCD: {{ gcd }}</div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def gcd():
    gcd = None
    if request.method == "POST":
        try:
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            gcd = gcd_euclid(num1, num2)
        except ValueError:
            gcd = "Invalid input!"
    return render_template_string(HTML_FORM, gcd=gcd)

if __name__ == "__main__":
    app.run(debug=True)
