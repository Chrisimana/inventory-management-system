from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QSpinBox,
    QGroupBox, QMessageBox
)
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont, QDoubleValidator

class FormInputBarang(QWidget):
    dataSubmitted = pyqtSignal(dict)
    formCleared = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.mode_tambah = True
        self.current_id = None
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Group box untuk form
        group_box = QGroupBox("Form Input Barang")
        group_box.setFont(QFont("Arial", 10, QFont.Bold))
        
        form_layout = QGridLayout()
        
        # Input fields
        self.nama_input = QLineEdit()
        self.nama_input.setPlaceholderText("Masukkan nama barang...")
        
        self.harga_input = QLineEdit()
        self.harga_input.setPlaceholderText("0")
        self.harga_input.setValidator(QDoubleValidator(0, 999999999, 2))
        
        self.kategori_combo = QComboBox()
        self.kategori_combo.addItems(["Elektronik", "Pakaian", "Makanan", "Minuman", "Alat Tulis", "Olahraga", "Kesehatan", "Umum"])
        
        self.stok_spin = QSpinBox()
        self.stok_spin.setRange(0, 9999)
        self.stok_spin.setValue(1)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.btn_submit = QPushButton("➕ Tambah Barang")
        self.btn_clear = QPushButton("🗑️ Bersihkan")
        
        self.btn_submit.clicked.connect(self.submit_data)
        self.btn_clear.clicked.connect(self.clear_form)
        
        button_layout.addWidget(self.btn_submit)
        button_layout.addWidget(self.btn_clear)
        
        # Add to form layout
        form_layout.addWidget(QLabel("Nama Barang:"), 0, 0)
        form_layout.addWidget(self.nama_input, 0, 1)
        form_layout.addWidget(QLabel("Harga (Rp):"), 1, 0)
        form_layout.addWidget(self.harga_input, 1, 1)
        form_layout.addWidget(QLabel("Kategori:"), 2, 0)
        form_layout.addWidget(self.kategori_combo, 2, 1)
        form_layout.addWidget(QLabel("Stok:"), 3, 0)
        form_layout.addWidget(self.stok_spin, 3, 1)
        
        group_box.setLayout(form_layout)
        layout.addWidget(group_box)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def submit_data(self):
        nama = self.nama_input.text().strip()
        harga_text = self.harga_input.text().strip()
        
        if not nama:
            QMessageBox.warning(self, "Peringatan", "Nama barang harus diisi!")
            self.nama_input.setFocus()
            return
        
        if not harga_text:
            QMessageBox.warning(self, "Peringatan", "Harga barang harus diisi!")
            self.harga_input.setFocus()
            return
        
        try:
            harga = float(harga_text)
        except ValueError:
            QMessageBox.warning(self, "Peringatan", "Format harga tidak valid!")
            self.harga_input.setFocus()
            return
        
        data = {
            'nama': nama,
            'harga': harga,
            'kategori': self.kategori_combo.currentText(),
            'stok': self.stok_spin.value()
        }
        
        if self.mode_tambah:
            self.dataSubmitted.emit(data)
            self.clear_form()
            QMessageBox.information(self, "Sukses", "Barang berhasil ditambahkan!")
        else:
            data['id'] = self.current_id
            self.dataSubmitted.emit(data)
            QMessageBox.information(self, "Sukses", "Barang berhasil diupdate!")
    
    def clear_form(self):
        self.nama_input.clear()
        self.harga_input.clear()
        self.kategori_combo.setCurrentIndex(0)
        self.stok_spin.setValue(1)
        self.set_tambah_mode()
        self.formCleared.emit()
    
    def set_tambah_mode(self):
        self.mode_tambah = True
        self.current_id = None
        self.btn_submit.setText("➕ Tambah Barang")
    
    def set_edit_mode(self, barang):
        self.mode_tambah = False
        self.current_id = barang.id
        self.nama_input.setText(barang.nama)
        self.harga_input.setText(str(int(barang.harga)))
        self.kategori_combo.setCurrentText(barang.kategori)
        self.stok_spin.setValue(barang.stok)
        self.btn_submit.setText("💾 Update Barang")