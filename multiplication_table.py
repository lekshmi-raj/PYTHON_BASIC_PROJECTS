from flask import Flask, request, render_template_string

app = Flask(__name__)

def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(f"{i} × {n} = {i * n}")
    return table

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
  <title>Multiplication Table</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f9fafb;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .container {
      background: white;
      padding: 30px 40px;
      border-radius: 12px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.1);
      width: 350px;
      text-align: center;
    }
    h2 {
      color: #4a4e69;
      margin-bottom: 20px;
    }
    input[type=number] {
      width: 100%;
      padding: 12px 15px;
      margin-bottom: 20px;
      border-radius: 8px;
      border: 1px solid #ddd;
      font-size: 16px;
      transition: border-color 0.3s;
    }
    input[type=number]:focus {
      border-color: #9a8c98;
      outline: none;
    }
    input[type=submit] {
      background-color: #22223b;
      color: white;
      border: none;
      padding: 12px 20px;
      font-size: 16px;
      border-radius: 8px;
      cursor: pointer;
      transition: background-color 0.3s;
      width: 100%;
    }
    input[type=submit]:hover {
      background-color: #4a4e69;
    }
    ul {
      text-align: left;
      padding-left: 0;
      list-style-type: none;
      margin-top: 20px;
    }
    ul li {
      background: #f2e9e4;
      padding: 8px 12px;
      margin-bottom: 6px;
      border-radius: 6px;
      font-weight: 600;
      color: #22223b;
      box-shadow: inset 2px 2px 5px rgba(255,255,255,0.6);
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Multiplication Table Generator</h2>
    <form method="POST">
      <input type="number" name="num" placeholder="Enter a number" required min="1">
      <input type="submit" value="Generate Table">
    </form>
    {% if table %}
      <ul>
        {% for line in table %}
          <li>{{ line }}</li>
        {% endfor %}
      </ul>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def multiplication():
    table = []
    if request.method == "POST":
        try:
            num = int(request.form["num"])
            table = multiplication_table(num)
        except ValueError:
            table = ["Invalid input! Please enter an integer."]
    return render_template_string(HTML_TEMPLATE, table=table)

if __name__ == "__main__":
    app.run(debug=True)
