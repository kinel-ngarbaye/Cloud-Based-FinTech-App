from fastapi import FastAPI, HTTPException

app = FastAPI()

# Simulated loan data
loan_db = {}

@app.post("/loan/request")
def request_loan(user_id: str, amount: float, interest_rate: float):
    if user_id in loan_db:
        raise HTTPException(status_code=400, detail="Active loan already exists")

    total_due = amount + (amount * interest_rate / 100)
    loan_db[user_id] = {"amount": amount, "interest_rate": interest_rate, "total_due": total_due}
    return {"message": "Loan approved", "total_due": total_due}

@app.get("/loan/status/{user_id}")
def loan_status(user_id: str):
    if user_id in loan_db:
        return loan_db[user_id]
    raise HTTPException(status_code=404, detail="No loan found")
