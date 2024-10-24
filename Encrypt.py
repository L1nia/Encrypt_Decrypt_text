from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import uc_crypt_gui
import sys

alphabet = '=>?@[\\]678hiVWlmABCDEpqrsjkJKL01234RюБжэяЩРтшЦМйu&UмоПtлС5хКцvЧёgчwSещFTвНZ#ОькТЖЯЁфбГъуЗиргШЪ$ЮХыЫIXHЕ!ВДG"Фа%АYсЙЬИздЛoxyz<MNOPQnУЭпн9abcdef^_`{|}~ \'()*+,-./:;'

class App(QMainWindow, uc_crypt_gui.Ui_UCrypt):
    def __init__(self):
        super().__init__()
        self.ui = uc_crypt_gui.Ui_UCrypt()
        self.ui.setupUi(self)
        self.ui.button_encrypt.clicked.connect(self.button_encrypt_clicked)
        self.ui.button_decrypt.clicked.connect(self.button_decrypt_clicked)
        
    def button_encrypt_clicked(self):
        key_to_encrypt = int(self.ui.msg_encrypt_key.toPlainText())
        msg_for_encrypt = self.ui.msg_to_encrypt.toPlainText()
        encrypted_text = ''

        for c in msg_for_encrypt:
            if c in alphabet:
                s1 = (alphabet.find(c) + key_to_encrypt) % len(alphabet)
                encrypted_text += alphabet[s1]
            else:
                encrypted_text += c
    
        self.ui.msg_encrypted.setText(encrypted_text)

    def button_decrypt_clicked(self):
        key_to_decrypt = int(self.ui.msg_decrypt_key.toPlainText())
        msg_for_decrypt = self.ui.msg_to_decrypt.toPlainText()
        decrypted_text = ''
        
        for c in msg_for_decrypt:
            if c in alphabet:
                s1 = (alphabet.find(c) - key_to_decrypt) % len(alphabet)
                decrypted_text += alphabet[s1]
            else:
                decrypted_text += c
                
        self.ui.msg_decrypted.setText(decrypted_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec()

