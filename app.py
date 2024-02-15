# Import libraries
from flask import Flask, render_template, request, url_for, redirect
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/create', methods=['GET', 'POST'])
def add_transaction():
    if request.method == "POST":
        transactions.append(
            {
             'id': len(transactions)+1,
             'date': request.form["date"],
             'amount': float(request.form["amount"])
            }
        )
        return redirect(url_for("get_transactions"))
    return render_template('form.html', transactions=transactions)

# Update operation
@app.route('/udate/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    date = request.form["date"]
    amount = request.form["amount"]
    if request.method == "POST":
        for transaction in transactions:
            if transaction["id"] = transaction_id:
                transaction["date"] = date
                transaction["amount"] = amount
    return render_template('edit.html', transactions=transactions)

# Delete operation
@app.route('/delete/<int:transaction_id>', methods=['GET', 'POST'])
def delete_transaction():
    if request.method == "POST":
        pass
    return render_template('transactions.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
