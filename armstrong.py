from flask import Flask, request, render_template_string

app = Flask(__name__)

def is_armstrong(n):
    n_str = str(n)
    power = len(n_str)
    total = sum(int(digit) ** power for digit in n_str)
    return total == n

HTML_TEMPLATE = '''
<!doctype html>
<html>
<head>
  <title>Armstrong Number Finder</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    body {
      margin: 0;
      height: 100vh;
      background: url('https://plus.unsplash.com/premium_photo-1718169446625-37680c0a3a0a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bnVtYmVyc3xlbnwwfHwwfHx8MA%3D%3D') no-repeat center center fixed;
      background-size: cover;
      font-family: 'Montserrat', sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      color: #fff;
    }
    .container {
      background: rgba(34, 34, 59, 0.85);
      padding: 40px 50px;
      border-radius: 15px;
      width: 360px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
      text-align: center;
    }
    h2 {
      color: #ffa500;
      margin-bottom: 25px;
      font-weight: 700;
      letter-spacing: 1.2px;
    }
    input[type=number] {
      width: 100%;
      padding: 12px 15px;
      margin-bottom: 20px;
      border-radius: 8px;
      border: none;
      font-size: 16px;
      outline: none;
    }
    input[type=submit] {
      background-color: #ff6600;
      color: white;
      border: none;
      padding: 12px 20px;
      font-size: 16px;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 700;
      transition: background-color 0.3s ease;
      width: 100%;
    }
    input[type=submit]:hover {
      background-color: #e65c00;
    }
    p.result {
      margin-top: 20px;
      font-size: 18px;
      font-weight: 600;
      color: #f0e68c;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Armstrong Number Finder</h2>
    <form method="POST">
      <input type="number" name="num" placeholder="Enter a number" required min="1" autofocus>
      <input type="submit" value="Check">
    </form>
    {% if result is not none %}
      <p class="result">{{ result }}</p>
    {% endif %}
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def armstrong():
    result = None
    if request.method == 'POST':
        try:
            num = int(request.form['num'])
            if is_armstrong(num):
                result = f"{num} is an Armstrong number!"
            else:
                result = f"{num} is not an Armstrong number."
        except ValueError:
            result = "Invalid input! Please enter a valid integer."
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
