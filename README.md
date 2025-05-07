# Novira Browser

**A minimal Python-based custom browser project using PyQt5.**  
Kullanıcıların kendi arama motorlarını ekleyebileceği sade ve özelleştirilebilir bir tarayıcı.

---

## 🌍 Features / Özellikler

- ✅ Built with **PyQt5 WebEngine**
- 🔍 Custom Search Engine selection
- ➕ Add/Edit/Delete your own search engines
- 🧠 Persistent settings (saved in `settings.json`)
- 🌐 Minimal toolbar: Back / Forward / Refresh / Go
- 🧩 Modular project structure (easy to expand)

---



## 🚀 Installation / Kurulum

### 1. Python ortamını oluşturun / Create Python virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Gerekli paketleri kurun / Install dependencies

```bash
pip install -r requirements.txt
```

> Eğer `requirements.txt` yoksa:  
> `pip freeze > requirements.txt` komutuyla oluşturabilirsin.

### 3. Uygulamayı çalıştırın / Run the app

```bash
python main.py
```

---

## 🗂️ Project Structure / Proje Yapısı

```
novira/
├── browser/
│   ├── main.py                 → Uygulama başlangıç dosyası
│   ├── toolbar.py              → Arayüz çubuğu (arama, geri, ileri...)
│   ├── webview.py              → Web görüntüleme modülü
│   ├── add_custom_search_dialog.py → Özel motor ekleme penceresi
├── config/
│   ├── search_engine.py        → Motor listesi ve ayarlar
│   ├── settings.json           → Kullanıcı tercihleri (JSON)
├── requirements.txt            → Gerekli Python kütüphaneleri
└── README.md
```

---

## 🧠 Future Ideas / Gelecek Fikirler

- 🔒 Dark mode
- 🗃️ Bookmark manager
- ⏱️ History system
- 🎨 Custom themes
- 📥 Download manager

