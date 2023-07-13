from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # initialisez la fenêtre et le label
        self.setWindowTitle("Longest Substring Without Repeating Characters Visualizer")
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 700, 500)

        # initialisez la chaîne et l'algorithme
        self.s = "votre_chaine"
        self.algo_state = {"start": 0, "end": 0, "longest": 0}  # change "" to 0

        # lancez l'algorithme
        self.timer = QTimer()
        self.timer.timeout.connect(self.run_algo)
        self.timer.start(1000)

    def run_algo(self):
        s = self.s  # change this from self.input_string to self.s
        data = set()
        start = 0
        end = 0

        while end < len(s):
            if s[end] not in data:
                data.add(s[end])
                end += 1
                self.algo_state['longest'] = max(self.algo_state['longest'], end - start)
                self.algo_state['start'] = start
                self.algo_state['end'] = end
                self.update_label()
            else:
                data.remove(s[start])
                start += 1
                self.algo_state['start'] = start
                self.update_label()

        self.timer.stop()  # stop the timer when the algorithm is done

    def update_label(self):
        self.label.setText(f"Start: {self.algo_state['start']}, End: {self.algo_state['end']}, Longest: {self.algo_state['longest']}")

app = QApplication([])
window = Window()
window.show()
app.exec_()
