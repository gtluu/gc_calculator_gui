import sys
from PyQt4 import QtGui, QtCore

def calculate_gc_content(sequence):
    return float((sequence.count('g') + sequence.count('c')) / len(sequence))

class gc_application(QtGui.QWidget):

    def __init__(self):
        super(gc_application, self).__init__()
        self.calc = None
        self.input_sequence_label = None
        self.input_sequence = None
        self.result = None
        self.init_gui()

    def init_gui(self):
        self.calc = QtGui.QPushButton('Calculate', self)
        self.calc.setToolTip('Calculate GC content.')
        self.input_sequence_label = QtGui.QLabel('Input Sequence')
        self.input_sequence = QtGui.QLineEdit()
        self.result = QtGui.QLabel()

        self.set_layout()
        self.setGeometry(400, 300, 500, 100)
        self.setWindowTitle('GC Content Calculator')
        self.setWindowIcon(QtGui.QIcon('blanka.png'))
        self.show()

        QtCore.QObject.connect(self.calc, QtCore.SIGNAL('clicked()'), self.calculate)

    def set_layout(self):
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.input_sequence_label, 1, 0)
        grid.addWidget(self.input_sequence, 2, 0)
        grid.addWidget(self.calc, 3, 0)
        grid.addWidget(self.result, 4, 0)
        self.setLayout(grid)

    def calculate(self):
        gc_value = (float((str(self.input_sequence.text()).lower().count('g') +
                           str(self.input_sequence.text()).lower().count('c'))) /\
                    float(len(str(self.input_sequence.text())))) * 100
        self.result.setText(str(gc_value) + '%')

def main():
    app = QtGui.QApplication(sys.argv)
    gc = gc_application()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()