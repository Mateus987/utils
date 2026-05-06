from flask import Flask, redirect
import requests
import json
import uuid

app = Flask(__name__)

@app.route("/redirect")
def gateway():
 
    session_id = str(uuid.uuid4()).replace("-", "")[0:17]

   
    url = "https://www.deolanebeauty.com.br/web_api/cart/"

    
    payload = {
        "Cart": {
            "session_id": session_id,
            "product_id": "38625687",  
            "quantity": "1",         
                                    
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

  
    response = requests.post(url, headers=headers, data=json.dumps(payload))

   
    print("Session ID gerado:", session_id)
    print("Resposta da API:", response.text)

    redirect_url = f"https://www.deolanebeauty.com.br/checkout/cart?session_id={session_id}&store_id=1374713&iniSession=1#carrinho"
    return redirect(redirect_url)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
