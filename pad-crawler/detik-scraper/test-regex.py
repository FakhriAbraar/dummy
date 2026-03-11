import re

# text = "Nomor saya 12345"
text = "https://news.detik.com/berita/d-8394275/5-fakta-pembunuh-ermanto-usman-di-bekasi-ditangkap-polisi"

hasil = re.search(r"\d+", text)

print(hasil.group())