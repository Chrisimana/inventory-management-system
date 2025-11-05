import json
import os
from datetime import datetime
from barang import Barang

class DatabaseHandler:
    def __init__(self, db_file='data_inventory.json'):
        self.db_file = db_file
        self.data = self._load_data()
    
    def _load_data(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {'barang': [], 'next_id': 1}
        return {'barang': [], 'next_id': 1}
    
    def _save_data(self):
        with open(self.db_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
    
    def tambah_barang(self, barang_data):
        barang = Barang.from_dict(barang_data)
        barang.id = self.data['next_id']
        barang.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        barang.updated_at = barang.created_at
        
        self.data['barang'].append(barang.to_dict())
        self.data['next_id'] += 1
        self._save_data()
        return barang.id
    
    def get_all_barang(self):
        return [Barang.from_dict(item) for item in self.data['barang']]
    
    def get_barang_by_id(self, id_barang):
        for item in self.data['barang']:
            if item['id'] == id_barang:
                return Barang.from_dict(item)
        return None
    
    def update_barang(self, id_barang, barang_data):
        for item in self.data['barang']:
            if item['id'] == id_barang:
                item.update(barang_data)
                item['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self._save_data()
                return True
        return False
    
    def hapus_barang(self, id_barang):
        self.data['barang'] = [item for item in self.data['barang'] if item['id'] != id_barang]
        self._save_data()
        return True
    
    def cari_barang(self, keyword):
        results = []
        for item in self.data['barang']:
            if (keyword.lower() in item['nama'].lower() or 
                keyword.lower() in item['kategori'].lower()):
                results.append(Barang.from_dict(item))
        return results