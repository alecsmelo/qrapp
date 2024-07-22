# Aplicativo para criação de QRCode
# Alecsandro Melo
# Versão 2.0

from PySide6 import QtWidgets as QW
from PySide6 import QtCore as QC
from PySide6 import QtGui as QG
import segno
import segno.helpers
from Include.layout import Ui_Janela

class JanelaPrincipal(QW.QWidget):
    def __init__(self):
        super(JanelaPrincipal, self).__init__()
        self.setWindowTitle("QRApp 2.0")

        #Instancia UI_janela como template 
        self.ui = Ui_Janela()
        self.ui.setupUi(self)

        #Chamada das funções pelo clique dos respectivos botões
        self.ui.btn_criar_qrlink.clicked.connect(self.criar_qr)
        self.ui.btn_criar_qrwifi.clicked.connect(self.criar_qrwifi)
        self.ui.btn_criar_qtcontato.clicked.connect(self.criar_qrcontato)
        self.ui.tema_escuro.clicked.connect(self.mudar_logo)

    #Método para que o usuário possa alterar a cor do logo
    def mudar_logo(self):
        
        if self.ui.tema_escuro.isChecked():
            self.ui.imagem_logo.setPixmap(QG.QPixmap(u"Include/logo2.png"))
            self.ui.icon = QG.QIcon()
            self.ui.icon.addFile(u"Include/icone2.ico", QC.QSize(), QG.QIcon.Mode.Normal, QG.QIcon.State.Off)
            self.setWindowIcon(self.ui.icon)
        
        else:
            self.ui.imagem_logo.setPixmap(QG.QPixmap(u"Include/logo.png"))
            self.ui.icon = QG.QIcon()
            self.ui.icon.addFile(u"Include/icone.ico", QC.QSize(), QG.QIcon.Mode.Normal, QG.QIcon.State.Off)
            self.setWindowIcon(self.ui.icon)


    #Método que usa a biblioteca Segno para criar QRCodes baseados em URL
    def criar_qr(self):
        opcao = QW.QFileDialog.Options()
        nome_arquivo, _ = QW.QFileDialog.getSaveFileName(self, "Salvar QRCode", "", "Formato PNG (*.png) ;; Formato SVG (*.svg)", options=opcao)
        if nome_arquivo:
            self.qr = segno.make(self.ui.entra_link.text(), micro=False)
            self.qr.save(nome_arquivo, scale=20)
            self.ui.rotulo_status.setText("QRCode foi salvo!")
        
        else:
            self.ui.rotulo_status.setText("QRCode não foi Criado")

    #Método que usar o segno para criação de QRCode para conexão wifi
    def criar_qrwifi(self):
        opcao = QW.QFileDialog.Options()
        nome_arquivo, _ = QW.QFileDialog.getSaveFileName(self, "Salvar QRCode", "", "Formato PNG (*.png) ;; Formato SVG (*.svg)", options=opcao)
        if nome_arquivo:
            self.qr = segno.helpers.make_wifi(ssid=self.ui.entra_ssid.text(), password=self.ui.entra_senha_wifi.text(), security=self.ui.cmb_escolhe_seguranca.currentText())
            self.qr.save(nome_arquivo, scale=20)
            self.ui.rotulo_status.setText("QRCode foi salvo!")
        
        else:
            self.ui.rotulo_status.setText("QRCode não foi Criado")

    #Método segno para criação de contato via QRCode
    def criar_qrcontato(self):
        opcao = QW.QFileDialog.Options()
        nome_arquivo, _ = QW.QFileDialog.getSaveFileName(self, "Salvar QRCode", "", "Formato PNG (*.png) ;; Formato SVG (*.svg)", options=opcao)
        if nome_arquivo:
            self.qr = segno.helpers.make_mecard(name=self.ui.entra_nome_contato.text(), phone=self.ui.entra_telefone_contato.text())
            self.qr.save(nome_arquivo, scale=20)
            self.ui.rotulo_status.setText("QRCode foi salvo!")
        
        else:
            self.ui.rotulo_status.setText("QRCode não foi Criado")


#Instanciar e rodar a aplicação em loop
if __name__ == '__main__':
    app = QW.QApplication([])
    rodar = JanelaPrincipal()
    rodar.show()
    app.exec()
