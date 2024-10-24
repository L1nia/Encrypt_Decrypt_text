from PyQt5 import QtCore, QtGui, QtWidgets

class CipherApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Калькулятор-шифратор-дешифратор')
        self.setGeometry(100, 100, 600, 400)

        
        layout = QtWidgets.QVBoxLayout()

        
        self.input_text = QtWidgets.QTextEdit(self)
        self.input_text.setPlaceholderText("Введите текст для шифрования/дешифрования")
        layout.addWidget(self.input_text)

        
        self.key_input = QtWidgets.QLineEdit(self)
        self.key_input.setPlaceholderText("Введите ключ (если требуется)")
        layout.addWidget(self.key_input)

        
        self.cipher_select = QtWidgets.QComboBox(self)
        self.cipher_select.addItems(["Цезаря", "Виженера", "Атбаш", "Плейфера", "Вернама"])
        layout.addWidget(self.cipher_select)

        
        self.encrypt_button = QtWidgets.QPushButton("Зашифровать", self)
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QtWidgets.QPushButton("Расшифровать", self)
        self.decrypt_button.clicked.connect(self.decrypt_text)
        layout.addWidget(self.decrypt_button)

        
        self.output_text = QtWidgets.QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def encrypt_text(self):
        text = self.input_text.toPlainText()
        key = self.key_input.text()
        cipher = self.cipher_select.currentText()

        if cipher == "Цезаря":
            result = self.caesar_encrypt(text, int(key))
        elif cipher == "Виженера":
            result = self.vigenere_encrypt(text, key)
        elif cipher == "Атбаш":
            result = self.atbash_encrypt(text)
        elif cipher == "Плейфера":
            result = self.playfair_encrypt(text, key)
        elif cipher == "Вернама":
            result = self.vigenere_encrypt(text, key)  # Placeholder for Vernam

        self.output_text.setPlainText(result)

    def decrypt_text(self):
        text = self.input_text.toPlainText()
        key = self.key_input.text()
        cipher = self.cipher_select.currentText()

        if cipher == "Цезаря":
            result = self.caesar_decrypt(text, int(key))
        elif cipher == "Виженера":
            result = self.vigenere_decrypt(text, key)
        elif cipher == "Атбаш":
            result = self.atbash_decrypt(text)
        else:
            result = text

            self.output_text.setPlainText(result)

    def caesar_encrypt(self, text, shift):
        encrypted = ""
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                new_char = chr((ord(char) - 65 + shift_amount) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift_amount) % 26 + 97)
                encrypted += new_char
            else:
                encrypted += char
        return encrypted

    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(text, -shift)

    def vigenere_encrypt(self, text, key):
        pass

    def vigenere_decrypt(self, text, key):
         pass

    def atbash_encrypt(self, text):
         return ''.join(chr(219 - ord(c)) if c.isalpha() else c for c in text)

    def atbash_decrypt(self, text):
         return self.atbash_encrypt(text)

    def playfair_encrypt(self, text, key):
         pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = CipherApp()
    ex.show()
    sys.exit(app.exec_())
