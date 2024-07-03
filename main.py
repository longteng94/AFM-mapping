
import sys

from PyQt5.QtWidgets import QApplication, QFileDialog
import wetting

app = QApplication(sys.argv)

file_path, _ = QFileDialog.getOpenFileName(caption='Select QI data')

#AFM QI data analysis
wetting.get_drop_prop(file_path)



