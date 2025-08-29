import os
import re

image_folder = "images"
html_file = "index.html"

# Lấy danh sách ảnh
files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
files.sort()

# Rename
count = 0
i = 1
for filename in files:
    new_name = f"{i}.jpeg"
    old_path = os.path.join(image_folder, filename)
    new_path = os.path.join(image_folder, new_name)
    # Nếu tên đã đúng format, bỏ qua
    if filename == new_name:
        i += 1
        continue

    while os.path.exists(new_path):
        i += 1
        new_name = f"{i}.jpeg"
        new_path = os.path.join(image_folder, new_name)

    os.rename(old_path, new_path)
    count += 1
    i += 1

print(f"Đã đổi tên {count} ảnh.")

# --- Update index.html ---
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Nếu đã có totalImages thì cập nhật, nếu chưa có thì thêm vào đầu hàm loadGallery
if "const totalImages =" in content:
    content = re.sub(r"const totalImages = \d+;", f"const totalImages = {count};", content)
else:
    content = re.sub(r"function loadGallery\(\) {", f"function loadGallery() {{\n      const totalImages = {count};", content)

print(f"Đã cập nhật index.html với totalImages = {count}")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

