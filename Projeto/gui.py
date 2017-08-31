from mainwindow import Ui_MainWindow
from controle import Controle

class GUI(Ui_MainWindow):
    def __init__(self):
        self.controle = Controle()

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.inputFileText.textChanged.connect(self.inputFileChanged)
        self.botaoOK.clicked.connect(self.carregarDados)
        self.qtdPalavraText.textChanged.connect(self.autocompletar)
        self.palavraText.textChanged.connect(self.autocompletar)

    def inputFileChanged(self):
        self.botaoOK.setEnabled(self.inputFileText.text().strip() != "")
    
    def carregarDados(self):
        self.controle.carregarDados(self.inputFileText.text())
        self.palavraText.setEnabled(True)
    
    def autocompletar(self):
        texto = self.palavraText.text()
        qtd = self.qtdPalavraText.text()
        if texto != "" and qtd != "":
            lista = self.controle.find(texto,int(qtd))
            self.outputText.setText(str(lista))            
        else:
            self.outputText.clear()
