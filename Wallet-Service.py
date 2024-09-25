from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory database for demonstration purposes
wallet_db = {
    "user1": {"balance": 1000.0, "transactions": []}
}

@app.get("/wallet/balance/{user_id}")
def get_balance(user_id: str):
    if user_id in wallet_db:
        return {"balance": wallet_db[user_id]["balance"]}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/wallet/transfer")
def transfer_funds(sender: str, receiver: str, amount: float):
    if sender not in wallet_db or receiver not in wallet_db:
        raise HTTPException(status_code=404, detail="User not found")

    if wallet_db[sender]["balance"] < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    wallet_db[sender]["balance"] -= amount
    wallet_db[receiver]["balance"] += amount
    wallet_db[sender]["transactions"].append({"to": receiver, "amount": amount})
    wallet_db[receiver]["transactions"].append({"from": sender, "amount": amount})
    return {"message": "Transfer successful", "sender_balance": wallet_db[sender]["balance"]}
