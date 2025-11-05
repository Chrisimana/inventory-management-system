import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QTabWidget, QMessageBox,
    QStatusBar, QToolBar, QAction, QSystemTrayIcon, QMenu
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QFont

from db_handler import DatabaseHandler
from table_widget import CustomTableWidget
from form_widget import FormInputBarang
from styles import setup_app_style, get_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseHandler()
        self.setup_ui()
        self.load_data()
        
    def setup_ui(self):
        self.setWindowTitle("🚀 Inventory Management System")
        self.setGeometry(100, 100, 1200, 800)
        
        # Setup central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Header
        header = QLabel("📦 INVENTORY MANAGE SYSTEM")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Arial", 20, QFont.Bold))
        header.setStyleSheet("color: #2c3e50; margin: 20px;")
        layout.addWidget(header)
        
        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Cari barang... (nama atau kategori)")
        self.search_input.textChanged.connect(self.cari_barang)
        
        btn_refresh = QPushButton("🔄 Refresh")
        btn_refresh.clicked.connect(self.load_data)
        
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(btn_refresh)
        layout.addLayout(search_layout)
        
        # Tab widget
        self.tab_widget = QTabWidget()
        
        # Tab 1: Data Barang
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)
        
        # Form dan tabel dalam split layout
        form_tabel_layout = QHBoxLayout()
        
        # Form input (kiri)
        self.form_widget = FormInputBarang()
        self.form_widget.dataSubmitted.connect(self.handle_data_submit)
        self.form_widget.formCleared.connect(self.load_data)
        
        # Tabel (kanan)
        self.table_widget = CustomTableWidget()
        self.table_widget.itemDeleted.connect(self.hapus_barang)
        self.table_widget.itemEdited.connect(self.edit_barang)
        
        form_tabel_layout.addWidget(self.form_widget, 1)
        form_tabel_layout.addWidget(self.table_widget, 2)
        
        tab1_layout.addLayout(form_tabel_layout)
        
        # Tab 2: Statistik
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)
        self.setup_statistik_tab(tab2_layout)
        
        self.tab_widget.addTab(tab1, "📊 Kelola Barang")
        self.tab_widget.addTab(tab2, "📈 Statistik")
        
        layout.addWidget(self.tab_widget)
        
        # Status bar
        self.statusBar().showMessage("✅ Sistem siap digunakan - Total barang: 0")
        
        # Setup toolbar
        self.setup_toolbar()
        
    def setup_toolbar(self):
        toolbar = QToolBar("Toolbar Utama")
        self.addToolBar(toolbar)
        
        # Aksi-aksi toolbar
        act_tambah = QAction("➕ Tambah Barang", self)
        act_refresh = QAction("🔄 Refresh", self)
        act_export = QAction("📤 Export Data", self)
        act_about = QAction("ℹ️ Tentang", self)
        
        act_tambah.triggered.connect(self.form_widget.clear_form)
        act_refresh.triggered.connect(self.load_data)
        act_export.triggered.connect(self.export_data)
        act_about.triggered.connect(self.show_about)
        
        toolbar.addAction(act_tambah)
        toolbar.addAction(act_refresh)
        toolbar.addAction(act_export)
        toolbar.addAction(act_about)
        
    def setup_statistik_tab(self, layout):
        # Placeholder untuk statistik
        stats_label = QLabel("📊 Fitur Statistik Akan Datang...\n")
        stats_label.setAlignment(Qt.AlignCenter)
        stats_label.setFont(QFont("Arial", 12))
        layout.addWidget(stats_label)
        
    def handle_data_submit(self, data):
        if 'id' in data:  # Mode edit
            if self.db.update_barang(data['id'], data):
                self.load_data()
                self.form_widget.set_tambah_mode()
        else:  # Mode tambah
            self.db.tambah_barang(data)
            self.load_data()
            
    def load_data(self):
        data_barang = self.db.get_all_barang()
        self.table_widget.update_table(data_barang)
        
        # Update status bar
        total_barang = len(data_barang)
        total_nilai = sum(barang.harga * barang.stok for barang in data_barang)
        self.statusBar().showMessage(
            f"✅ Sistem siap digunakan - Total barang: {total_barang} | "
            f"Total nilai inventory: Rp {total_nilai:,.0f}".replace(",", ".")
        )
        
    def hapus_barang(self, id_barang):
        if self.db.hapus_barang(id_barang):
            self.load_data()
            QMessageBox.information(self, "Sukses", "Barang berhasil dihapus!")
            
    def edit_barang(self, id_barang):
        barang = self.db.get_barang_by_id(id_barang)
        if barang:
            self.form_widget.set_edit_mode(barang)
            
    def cari_barang(self):
        keyword = self.search_input.text().strip()
        if keyword:
            results = self.db.cari_barang(keyword)
            self.table_widget.update_table(results)
        else:
            self.load_data()
            
    def export_data(self):
        QMessageBox.information(self, "Export Data", 
                              "Fitur export data akan segera hadir!\n"
                              "Format: Excel, PDF, CSV")
        
    def show_about(self):
        QMessageBox.about(self, "Tentang Aplikasi",
                        "🚀 Inventory Management System\n"
                        "Fitur Utama:\n"
                        "• Manajemen barang lengkap\n"
                        "• Pencarian real-time\n"
                        "• History otomatis\n"
                        "• Backup data JSON\n"
                        "• Interface modern\n\n"
                        )

def main():
    app = QApplication(sys.argv)
    
    # Setup styling
    setup_app_style(app)
    app.setStyleSheet(get_stylesheet())
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()