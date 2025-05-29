from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


##Caesar
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods =['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return render_template("caesar.html", outputCipherText = encrypted_text , inputPlainText = text, inputKeyPlain = key)

@app.route("/decrypt", methods =['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return render_template("caesar.html", outputPlainText = decrypted_text , inputCipherText = text, inputKeyCipher = key)

##Vigenere
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods =['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return render_template("vigenere.html", outputCipherText = encrypted_text , inputPlainText = text, inputKeyPlain = key)

@app.route("/vigenere/decrypt", methods =['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return render_template("vigenere.html", outputPlainText = decrypted_text , inputCipherText = text, inputKeyCipher = key)


##Railfence
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods =['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Railfence = RailFenceCipher()
    encrypted_text = Railfence.rail_fence_encrypt(text, key)
    return render_template("railfence.html", outputCipherText = encrypted_text , inputPlainText = text, inputKeyPlain = key)

@app.route("/railfence/decrypt", methods =['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Railfence = RailFenceCipher()
    decrypted_text = Railfence.rail_fence_decrypt(text, key)
    return render_template("railfence.html", outputPlainText = decrypted_text , inputCipherText = text, inputKeyCipher = key)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 5050, debug=True)