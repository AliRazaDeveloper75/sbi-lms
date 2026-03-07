import urllib.request
pages = ['about', 'contact', 'services', 'courses']
for page in pages:
    try:
        resp = urllib.request.urlopen(f"http://127.0.0.1:8000/{page}/")
        print(f"Page: {page}, Status: {resp.status}")
    except Exception as e:
        print(f"Page: {page}, Error: {e}")
