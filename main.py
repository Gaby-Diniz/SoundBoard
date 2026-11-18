import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

#Criar aplicação
app = QApplication(sys.argv)

#Criar janela
janela = QWidget()

#Definir tamanho da janela
janela.setWindowTitle("Soundboard")
janela.resize(900, 600)


# criar grade dos botoes
grade = QGridLayout()

# Criar 12 botões
for i in range(12):
    botao = QPushButton(f"som {i+1}")
    botao.setToolTip(f"som {i+1}")

    linha = i // 4  # calcula a linha (0, 1, 2)
    coluna = i % 4  # calcula a coluna (0, 1, 2, 3)

    grade.addWidget(botao, linha, coluna)  # adiciona o botão à grade


#Adicionar a grade à janela
janela.setLayout(grade)


#exibir janela
janela.show()


#manter a aplicação aberta
sys.exit(app.exec())
