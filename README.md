# 🚀 Inventory Management System

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-green)
![License](https://img.shields.io/badge/license-MIT-success)

**Sistem manajemen inventory dengan GUI modern untuk mengelola barang dagangan secara profesional**

[Fitur](#-fitur-unggulan) • [Instalasi](#-instalasi) • [Penggunaan](#-penggunaan) • [Dokumentasi](#-dokumentasi)

</div>

## 📋 Daftar Isi

- [Gambaran Umum](#-gambaran-umum)
- [Fitur Unggulan](#-fitur-unggulan)
- [Instalasi](#-instalasi)
- [Penggunaan](#-penggunaan)
- [Dokumentasi](#-dokumentasi)
- [Contoh Penggunaan](#-contoh-penggunaan)
- [FAQ](#-faq)

## 🎯 Gambaran Umum

**Inventory Management System** adalah aplikasi manajemen stok barang yang dibangun dengan Python dan PyQt5, menawarkan solusi lengkap untuk mengelola inventory bisnis Anda. Aplikasi ini memiliki antarmuka modern yang intuitif dan fitur-fitur canggih untuk efisiensi operasional.

### ✨ Highlights

- 🎨 **GUI Modern** dengan tema profesional dan responsive design
- 💾 **Database Persisten** dengan penyimpanan JSON otomatis
- 🔍 **Pencarian Real-time** untuk akses data cepat
- 📊 **Manajemen Stok** dengan color coding dan alert
- 🚀 **CRUD Lengkap** - Create, Read, Update, Delete
- 📈 **Statistik Real-time** nilai inventory

## 🌟 Fitur Unggulan

### 📦 Core Inventory Management
- **Manajemen Barang Lengkap** - Tambah, edit, hapus, dan lihat data barang
- **Kategori Barang** - Organisasi barang berdasarkan kategori
- **Management Stok** - Monitoring stok dengan warning system
- **Auto-increment ID** - Penomoran otomatis yang terorganisir

### 🔍 Advanced Search & Filter
- **Pencarian Real-time** - Cari berdasarkan nama atau kategori
- **Filter Data** - Temukan barang dengan cepat
- **Sorting Otomatis** - Urutkan data berdasarkan kolom
- **Live Search** - Hasil langsung terupdate saat mengetik

### 💾 Data Management
- **Auto-save** - Data tersimpan otomatis ke JSON file
- **Backup Otomatis** - Data aman dengan persistent storage
- **Export Ready** - Persiapan fitur export ke Excel/PDF/CSV
- **History Tracking** - Timestamp create dan update

### 🎨 User Experience
- **Modern GUI** - Interface profesional dengan PyQt5
- **Context Menu** - Klik kanan untuk akses cepat
- **Keyboard Shortcuts** - Navigasi efisien
- **Responsive Design** - Adaptif berbagai ukuran layar
- **Color Coding** - Stok rendah berwarna warning

### ⚙️ System Features
- **Form Validation** - Validasi input yang robust
- **Error Handling** - Penanganan error yang elegan
- **Confirmation Dialog** - Konfirmasi untuk operasi kritis
- **Status Bar** - Informasi real-time sistem

### Fitur Interaktif

- **🎯 Context Menu** - Klik kanan untuk edit/hapus
- **🔍 Live Search** - Ketik langsung untuk mencari
- **📊 Real-time Stats** - Total barang dan nilai inventory
- **🎨 Color Alert** - Stok rendah berwarna kuning/merah

## 📥 Instalasi

### Prerequisites

- Python 3.7 atau lebih tinggi
- pip (Python package manager)

### Step-by-Step Installation

1. **Download atau Clone Project**
   ```bash
   git clone https://github.com/username/super-inventory-system.git
   cd super-inventory-system
   ```

2. **Buat Virtual Environment (Recommended)**
   ```bash
   python -m venv inventory_env
   # Windows
   inventory_env\Scripts\activate
   # Linux/Mac
   source inventory_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install PyQt5
   ```

4. **Verifikasi Instalasi**
   ```bash
   python main.py
   ```

### Quick Install (Windows)
```bash
# Download project, ekstrak, dan jalankan:
python main.py
```

### Requirements File
```txt
PyQt5==5.15.9
```

## 🎮 Penggunaan

### Menjalankan Aplikasi

```bash
python main.py
```

### Basic Operations

1. **Menambah Barang Baru**
   - Isi form di sebelah kiri
   - Klik "➕ Tambah Barang"
   - Data otomatis tersimpan

2. **Mengedit Barang**
   - Klik kanan pada barang di tabel
   - Pilih "✏️ Edit Barang"
   - Ubah data di form, klik "💾 Update Barang"

3. **Menghapus Barang**
   - Klik kanan pada barang
   - Pilih "🗑️ Hapus Barang"
   - Konfirmasi penghapusan

4. **Mencari Barang**
   - Ketik di search bar "🔍 Cari barang..."
   - Hasil langsung terfilter real-time

### Form Input Fields

| Field | Type | Validation |
|-------|------|------------|
| Nama Barang | Text | Required |
| Harga | Number | Required, numeric |
| Kategori | Dropdown | Predefined categories |
| Stok | Spinbox | 0-9999 |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Submit form |
| `Ctrl + F` | Focus ke search box |
| `Ctrl + R` | Refresh data |
| `Delete` | Hapus item selected |
| `Esc` | Clear form |

## 📚 Dokumentasi Teknis

### File Descriptions

| File | Description |
|------|-------------|
| `main.py` | Entry point aplikasi, mengatur GUI utama |
| `barang.py` | Data class untuk representasi barang |
| `db_handler.py` | Handler untuk operasi database JSON |
| `table_widget.py` | Custom table dengan context menu |
| `form_widget.py` | Form input dengan validasi |
| `styles.py` | Styling dan theme configuration |
    
## 💡 Contoh Penggunaan

### Scenario 1: Retail Store
```
➊ Tambah produk baru: "Sepatu Nike", Rp 500.000, Kategori: Olahraga, Stok: 10
➋ Update stok: Stok berkurang jadi 5 setelah penjualan
➌ Cari produk: Ketik "nike" di search box
➍ Hapus produk: Jika sudah tidak dijual lagi
```

### Scenario 2: Warehouse Management
```
➊ Import data barang dalam jumlah besar
➋ Monitor stok rendah (warna kuning/merah)
➌ Cek total nilai inventory di status bar
➍ Export data untuk laporan bulanan
```

### Sample Data Operations

```python
# Menambah barang
data = {
    'nama': 'Monitor LCD 24inch',
    'harga': 2500000,
    'kategori': 'Elektronik', 
    'stok': 15
}
db_handler.tambah_barang(data)

# Mencari barang
results = db_handler.cari_barang('monitor')
for barang in results:
    print(f"{barang.nama} - Rp {barang.harga}")
```

## ❓ FAQ

### Q: Apakah data tersimpan secara otomatis?
**A:** Ya! Semua perubahan langsung tersimpan ke file JSON secara otomatis.

### Q: Bisakah import data dari Excel?
**A:** Saat ini belum, tapi fitur import/export sedang dalam pengembangan.

### Q: Berapa jumlah maksimal barang yang bisa dikelola?
**A:** Tidak ada batasan praktis, sistem bisa menangani ribuan barang.

### Q: Apakah bisa diinstall di komputer tanpa Python?
**A:** Bisa dengan cara di-build menjadi executable menggunakan PyInstaller.

### Q: Bagaimana backup data?
**A:** Cukup backup file `data_inventory.json` secara manual.

### Q: Support database selain JSON?
**A:** Architecture sudah modular, bisa dikembangkan untuk MySQL/PostgreSQL.

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'PyQt5'**
   ```bash
   pip install PyQt5
   ```

2. **JSON file corruption**
   - Delete `data_inventory.json` (akan dibuat ulang otomatis)

3. **GUI not responding**
   - Restart aplikasi
   - Check memory usage

### Performance Tips

- Untuk data sangat besar (>10,000 items), pertimbangkan virtual scrolling
- Gunakan SSD untuk storage yang lebih cepat
- Tutup aplikasi lain untuk optimal performance

<div align="center">

**⭐ Jika project ini membantu Anda, jangan lupa beri bintang! ⭐**

[Kembali ke Atas](#-inventory-management-system)

</div>