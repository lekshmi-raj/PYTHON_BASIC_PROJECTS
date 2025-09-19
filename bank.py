from flask import Flask, request, render_template_string

app = Flask(__name__)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"You deposited {amount}."
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"You successfully withdrew {amount}. Your balance is {self.balance}."

# Create a bank account instance
account = BankAccount("ansil", 1000)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        action = request.form.get("action")
        amount = request.form.get("amount")
        if amount and amount.isdigit():
            amount = int(amount)
            if action == "deposit":
                message = account.deposit(amount)
            elif action == "withdraw":
                message = account.withdraw(amount)
        else:
            message = "Please enter a valid amount."
    
    html = """
    <html>
<head>
<title>Bank Account</title>
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 0;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container {
        background: white;
        padding: 40px 50px;
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
        max-width: 400px;
        width: 90%;
        text-align: center;
    }

    h2 {
        color: #4a148c;
        margin-bottom: 20px;
        font-weight: 700;
    }

    .balance {
        font-size: 20px;
        color: #6a1b9a;
        margin-bottom: 30px;
        font-weight: 500;
        letter-spacing: 1.2px;
    }

    input[type=number] {
        width: 100%;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #ce93d8;
        font-size: 16px;
        margin-bottom: 25px;
        outline: none;
        transition: 0.3s;
    }

    input[type=number]:focus {
        border-color: #7e57c2;
        box-shadow: 0 0 8px #9575cd;
    }

    button {
        width: 48%;
        padding: 15px 0;
        margin: 0 1%;
        border: none;
        border-radius: 10px;
        font-weight: 700;
        font-size: 16px;
        cursor: pointer;
        color: white;
        box-shadow: 0 7px 14px rgba(122, 64, 255, 0.35);
        transition: all 0.3s ease;
    }

    .btn-deposit {
        background: #8e24aa;
    }

    .btn-deposit:hover {
        background: #6a1b9a;
        box-shadow: 0 7px 25px rgba(106, 27, 154, 0.6);
    }

    .btn-withdraw {
        background: #d81b60;
    }

    .btn-withdraw:hover {
        background: #ad1457;
        box-shadow: 0 7px 25px rgba(173, 20, 87, 0.6);
    }

    .message {
        margin-top: 30px;
        font-weight: 700;
        font-size: 16px;
        color: #4a148c;
        min-height: 24px;
    }

    .header-image {
        width: 100px;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 1px #4a148c);
    }
</style>
</head>
<body>
<div class="container">
    <img src="https://cdn-icons-png.flaticon.com/512/1995/1995565.png" alt="Bank Icon" class="header-image">
    <h2>Bank Account of {{ owner }}</h2>
    <div class="balance">Balance: {{ balance }}</div>
    <form method="POST">
        <input type="number" name="amount" placeholder="Enter amount" required min="1">
        <div>
            <button type="submit" name="action" value="deposit" class="btn-deposit">Deposit</button>
            <button type="submit" name="action" value="withdraw" class="btn-withdraw">Withdraw</button>
        </div>
    </form>
    {% if message %}
        <div class="message">{{ message }}</div>
    {% endif %}
</div>
</body>
</html>
    """
    return render_template_string(html, owner=account.owner, balance=account.balance, message=message)

if __name__ == "__main__":
    app.run(debug=True)
