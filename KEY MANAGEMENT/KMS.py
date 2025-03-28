from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, dh
from cryptography.hazmat.primitives import serialization
import ssl

app = Flask(__name__)

# --- SYMMETRIC KEY MANAGEMENT (AES) ---
def generate_symmetric_key():
    return Fernet.generate_key()

symmetric_keys = {}

@app.route('/generate_symmetric_key', methods=['POST'])
def generate_aes_key():
    client_id = request.json.get("client_id")
    key = generate_symmetric_key()
    symmetric_keys[client_id] = key.decode()
    return jsonify({"client_id": client_id, "symmetric_key": key.decode()})

# --- ASYMMETRIC KEY MANAGEMENT (RSA) ---
def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

rsa_keys = {}

@app.route('/generate_rsa_key', methods=['POST'])
def generate_rsa():
    client_id = request.json.get("client_id")
    private_key, public_key = generate_rsa_key_pair()
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    rsa_keys[client_id] = {"private": private_pem.decode(), "public": public_pem.decode()}
    return jsonify({"client_id": client_id, "public_key": public_pem.decode()})

# --- DIFFIE-HELLMAN KEY EXCHANGE ---
dh_parameters = dh.generate_parameters(generator=2, key_size=2048)

def generate_dh_key_pair():
    private_key = dh_parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

dh_keys = {}

@app.route('/generate_dh_key', methods=['POST'])
def generate_dh():
    client_id = request.json.get("client_id")
    private_key, public_key = generate_dh_key_pair()
    dh_keys[client_id] = {"private": private_key, "public": public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()}
    return jsonify({"client_id": client_id, "public_key": dh_keys[client_id]["public"]})

# --- KEY REVOCATION SYSTEM ---
revoked_keys = set()

@app.route('/revoke_key', methods=['POST'])
def revoke_key():
    key_id = request.json.get("key_id")
    revoked_keys.add(key_id)
    return jsonify({"message": f"Key {key_id} revoked."})

@app.route('/check_key_status', methods=['POST'])
def check_key_status():
    key_id = request.json.get("key_id")
    status = "Revoked" if key_id in revoked_keys else "Active"
    return jsonify({"key_id": key_id, "status": status})

# --- RUNNING SECURE SERVER ---
if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('server.crt', 'server.key')  # Provide your own certificates
    app.run(host='0.0.0.0', port=5000, ssl_context=context)
