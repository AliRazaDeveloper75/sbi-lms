import re
import urllib.parse

phone = "923043309005"
msg = "Contact from website and I am interesting in a course, please give me details."
encoded_msg = urllib.parse.quote(msg)
wa_url = f"https://wa.me/{phone}?text={encoded_msg}"

files = [
    r"d:\SBI NAVTTC\Node.JS\SBI LMS\templates\landing\index.html",
    r"d:\SBI NAVTTC\Node.JS\SBI LMS\templates\landing\courses.html"
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace href link for enroll buttons.
    old_link = r'''<a href="{% url 'login' %}" class="btn btn-gradient w-100 mt-auto rounded-pill py-2 fw-bold">Enroll Now <i class="fas fa-arrow-right ms-2 fs-6"></i></a>'''
    new_link = f'''<a href="{wa_url}" target="_blank" class="btn btn-gradient w-100 mt-auto rounded-pill py-2 fw-bold">Enroll Now <i class="fab fa-whatsapp ms-2 fs-6"></i></a>'''
    content = content.replace(old_link, new_link)
    
    # Update duration in courses.html
    if 'courses.html' in fpath:
        content = re.sub(r'<span><i class="far fa-clock me-1"></i> \d+ Weeks</span>', r'<span><i class="far fa-clock me-1"></i> 3 Months</span>', content)
        
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated templates successfully.")
