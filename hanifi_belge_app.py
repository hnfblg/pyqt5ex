import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QCheckBox, QProgressBar, QMenuBar, 
                             QAction, QToolBar, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class HanifiBelgeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Pencere ayarları
        self.setWindowTitle("Hanifi Belge")
        self.setGeometry(300, 300, 400, 300)
        
        # Progress bar için değer takibi
        self.progress_value = 0
        
        # UI bileşenlerini oluştur
        self.init_ui()
        
    def init_ui(self):
        """Ana arayüzü oluşturur"""
        # Ana widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # CheckBox oluştur
        self.checkbox = QCheckBox("Butonu etkinleştir")
        self.checkbox.setChecked(False)  # Başlangıçta seçili değil
        self.checkbox.stateChanged.connect(self.checkbox_changed)
        layout.addWidget(self.checkbox)
        
        # Push Button oluştur
        self.push_button = QPushButton("İlerleme Çubuğunu Artır (+%25)")
        self.push_button.setEnabled(False)  # Başlangıçta pasif
        self.push_button.clicked.connect(self.button_clicked)
        layout.addWidget(self.push_button)
        
        # Progress Bar oluştur
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        # Layout'a boşluk ekle
        layout.addStretch()
        
        # Menü çubuğunu oluştur
        self.create_menu_bar()
        
        # Araç çubuğunu oluştur
        self.create_toolbar()
        
    def create_menu_bar(self):
        """Menü çubuğunu oluşturur"""
        menubar = self.menuBar()
        
        # File menüsü
        file_menu = menubar.addMenu('File')
        
        # Exit aksiyonu
        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Uygulamadan çık')
        exit_action.triggered.connect(self.close_application)
        
        file_menu.addAction(exit_action)
        
    def create_toolbar(self):
        """Araç çubuğunu oluşturur"""
        toolbar = QToolBar("Ana Araç Çubuğu")
        self.addToolBar(toolbar)
        
        # Exit butonu için aksiyon
        exit_action = QAction('Exit', self)
        exit_action.setStatusTip('Uygulamadan çık')
        exit_action.triggered.connect(self.close_application)
        
        # Toolbar'a exit aksiyonunu ekle
        toolbar.addAction(exit_action)
        
    def checkbox_changed(self, state):
        """CheckBox durumu değiştiğinde çağırılır"""
        if state == Qt.Checked:
            self.push_button.setEnabled(True)  # Butonu etkinleştir
        else:
            self.push_button.setEnabled(False)  # Butonu pasif yap
            
    def button_clicked(self):
        """Push button'a tıklandığında çağırılır"""
        # Progress bar değerini %25 artır
        self.progress_value += 25
        
        # Maksimum değeri aşmasını engelle
        if self.progress_value > 100:
            self.progress_value = 100
            
        # Progress bar'ı güncelle
        self.progress_bar.setValue(self.progress_value)
        
        # %100'e ulaştığında bilgi mesajı göster
        if self.progress_value >= 100:
            QMessageBox.information(self, "Bilgi", "Progress bar %100'e ulaştı!")
            
    def close_application(self):
        """Uygulamayı kapatır"""
        reply = QMessageBox.question(self, 'Çıkış', 
                                   'Uygulamadan çıkmak istediğinizden emin misiniz?',
                                   QMessageBox.Yes | QMessageBox.No, 
                                   QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.close()


def main():
    """Ana fonksiyon - Uygulamayı başlatır"""
    # QApplication instance oluştur
    app = QApplication(sys.argv)
    
    # Ana pencereyi oluştur ve göster
    window = HanifiBelgeApp()
    window.show()
    
    # Uygulama döngüsünü başlat
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
