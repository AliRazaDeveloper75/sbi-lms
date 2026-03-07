import os

replacements = {
    "Lecturers": "Teacher Instructors",
    "Lecturer": "Teacher Instructor",
    "lecturers": "teacher instructors",
    # Specific ones for lowercase text if any
}

template_dir = r"d:\SBI NAVTTC\Node.JS\SBI LMS\templates"

# We want to avoid replacing variable names, so we'll be careful.
# But replacing "Lecturers" and "Lecturer" in HTML almost exclusively affects user-facing text and sometimes class/id names (which we might not want to break).
# Wait, "Lecturer" with uppercase L is mostly text strings or trans tags.
# Let's do a safe string replacement for specific known strings first.

safe_replacements = {
    "Lecturers": "Teacher Instructors",
    "Lecturer": "Teacher Instructor",
    "lecturer qualifications": "teacher instructor qualifications",
}

for root, dirs, files in os.walk(template_dir):
    for filename in files:
        if filename.endswith(".html"):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Since 'Lecturers' contains 'Lecturer', order matters.
            content = content.replace("Lecturers", "Teacher Instructors")
            content = content.replace("Lecturer", "Teacher Instructor")
            content = content.replace("lecturer qualifications", "teacher instructor qualifications")
            content = content.replace("CRUD (Create, Retrieve, Update &amp; Delete) lecturers", "CRUD (Create, Retrieve, Update &amp; Delete) teacher instructors")
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filepath}")

print("Replacement complete in templates.")
