from flask import Flask, redirect
import requests
import json
import uuid

app = Flask(__name__)

@app.route("/redirect")
def gateway():
    # Gerar um session_id aleatório sem traços
    session_id = str(uuid.uuid4()).replace("-", "")

    # Endpoint da API
    url = "https://www.futfanatics.com.br/web_api/cart/"

    # Payload para criar o carrinho com o produto
    payload = {
        "Cart": {
            "session_id": session_id,
            "product_id": "165697",   # ID do produto
            "quantity": "1",          # Quantidade
            "variant_id": "2152337"   # Variante do produto
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    # Enviar requisição para a API
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Debug no console
    print("Session ID gerado:", session_id)
    print("Resposta da API:", response.text)

    # Redirecionar para o carrinho do cliente com o session_id
    redirect_url = f"https://www.futfanatics.com.br/checkout/cart?session_id={session_id}&store_id=311840&iniSession=1#carrinho"
    return redirect(redirect_url)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
