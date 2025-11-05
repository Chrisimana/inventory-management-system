from PyQt5.QtWidgets import (
    QTableWidget, QTableWidgetItem, QHeaderView, QMenu, QAction,
    QMessageBox, QAbstractItemView
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QBrush

class CustomTableWidget(QTableWidget):
    itemDeleted = pyqtSignal(int)
    itemEdited = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_context_menu()
    
    def setup_ui(self):
        self.setColumnCount(6)
        self.setHorizontalHeaderLabels([
            "ID", "Nama Barang", "Harga", "Kategori", "Stok", "Terakhir Diupdate"
        ])
        
        # Styling table
        header = self.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(5, QHeaderView.Stretch)
        
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # Set font
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
    
    def setup_context_menu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
    
    def show_context_menu(self, position):
        menu = QMenu(self)
        
        edit_action = QAction("✏️ Edit Barang", self)
        delete_action = QAction("🗑️ Hapus Barang", self)
        
        edit_action.triggered.connect(self.edit_selected_item)
        delete_action.triggered.connect(self.delete_selected_item)
        
        menu.addAction(edit_action)
        menu.addAction(delete_action)
        
        menu.exec_(self.viewport().mapToGlobal(position))
    
    def edit_selected_item(self):
        current_row = self.currentRow()
        if current_row >= 0:
            item_id = int(self.item(current_row, 0).text())
            self.itemEdited.emit(item_id)
    
    def delete_selected_item(self):
        current_row = self.currentRow()
        if current_row >= 0:
            item_id = int(self.item(current_row, 0).text())
            item_name = self.item(current_row, 1).text()
            
            reply = QMessageBox.question(
                self, 'Konfirmasi Hapus',
                f'Apakah Anda yakin ingin menghapus "{item_name}"?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                self.itemDeleted.emit(item_id)
    
    def update_table(self, data_barang):
        self.setRowCount(0)
        
        for barang in data_barang:
            row = self.rowCount()
            self.insertRow(row)
            
            # Format harga dengan separator ribuan
            harga_text = f"Rp {barang.harga:,.0f}".replace(",", ".")
            
            # Warna stok
            stok_item = QTableWidgetItem(str(barang.stok))
            if barang.stok == 0:
                stok_item.setBackground(QBrush(QColor(255, 200, 200)))  # Merah muda untuk stok 0
            elif barang.stok < 5:
                stok_item.setBackground(QBrush(QColor(255, 255, 200)))  # Kuning untuk stok rendah
            
            items = [
                QTableWidgetItem(str(barang.id)),
                QTableWidgetItem(barang.nama),
                QTableWidgetItem(harga_text),
                QTableWidgetItem(barang.kategori),
                stok_item,
                QTableWidgetItem(barang.updated_at)
            ]
            
            for col, item in enumerate(items):
                item.setTextAlignment(Qt.AlignCenter)
                self.setItem(row, col, item)