import feedparser
import json

# URL RSS Google Trends Indonesia
url = "https://trends.google.com/trending/rss?geo=ID"
feed = feedparser.parse(url)

# 1. Siapkan list kosong untuk menampung data
trends_data = []

# 2. For loop untuk membangun struktur dictionary baru
for entry in feed.entries:
    # Membuat objek dictionary untuk setiap baris tren
    item = {
        "topik": entry.title,
        "estimasi_pencarian": entry.get('ht_approx_traffic'),
        "link_berita": entry.get('ht_news_item_url'), # Akan bernilai None jika tidak ada
        "tanggal_terbit": entry.published
    }
    
    # Masukkan ke dalam list
    trends_data.append(item)

# 3. Konversi list tersebut menjadi format JSON (Pretty Print)
json_output = json.dumps(trends_data, indent=4, ensure_ascii=False)

# (Opsional) Simpan ke file .json
with open("google-trends-scraper-rss/data/google_trends_id.json", "w", encoding="utf-8") as f:
    f.write(json_output)