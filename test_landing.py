import urllib.request
try:
    resp = urllib.request.urlopen("http://127.0.0.1:8000/")
    print("Status:", resp.status)
    content = resp.read().decode('utf-8')
    print("Content length:", len(content))
    print("Contains 'School of Business Intelligence':", "School of Business Intelligence" in content)
    print("Contains 'Premium IT Services':", "Premium IT Services" in content)
    print("Contains 'Featured Training Programs':", "Featured Training Programs" in content)
    print("Contains 'Login / Access LMS':", "Login / Access LMS" in content)
except Exception as e:
    print("Error:", e)
