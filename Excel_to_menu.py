import csv

# يقرأ ملف المنتجات
with open('products.csv', encoding='utf-8') as f:
    products = list(csv.DictReader(f))

# يبني كروت HTML
cards_html = ""
for p in products:
    cards_html += f"""
    <div class="card">
      <h3>{p['name']}</h3>
      <p>{p['price']} ريال</p>
    </div>
    """

# قالب الموقع الكامل
html_template = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>منيو تلقائي</title>
<link rel="stylesheet" href="style.css"></head>
<body>
<h1 style="text-align:center;padding:20px">تم إنشاء المنيو آلياً من Excel</h1>
<div class="cards">{cards_html}</div>
</body></html>
"""

with open('menu.html','w',encoding='utf-8') as out:
    out.write(html_template)

print("✅ تم إنشاء menu.html بنجاح - افتحه في المتصفح")
