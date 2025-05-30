from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayFairCipher
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

##Tranposition
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods =['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Transposition = TranspositionCipher()
    encrypted_text = Transposition.encrypt(text, key)
    return render_template("transposition.html", outputCipherText = encrypted_text , inputPlainText = text, inputKeyPlain = key)

@app.route("/transposition/decrypt", methods =['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)
    return render_template("transposition.html", outputPlainText = decrypted_text , inputCipherText = text, inputKeyCipher = key)

##PlayFair
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/creatematrix", methods=['POST'])
def playfair_creatematrixkey():
    key = request.form['inputKey']
    PlayFair = PlayFairCipher()
    key_matrix = PlayFair.create_playfair_matrix(key)
    return render_template("playfair.html", outputKeyMatrix = key_matrix, inputKey = key)

@app.route("/playfair/encrypt", methods =['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    PlayFair = PlayFairCipher()
    encrypted_text = PlayFair.playfair_encrypt(text, key)
    return render_template("playfair.html", outputCipherText = encrypted_text , inputPlainText = text, inputKeyPlain = key)

@app.route("/transposition/decrypt", methods =['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)
    return render_template("transposition.html", outputPlainText = decrypted_text , inputCipherText = text, inputKeyCipher = key)






if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 5050, debug=True)