# SBI LMS (Learning Management System)

Welcome to **SBI LMS**, a feature-rich, modern Learning Management System designed for educational organizations and individual learners.

![SBI LMS Logo](https://github.com/AliRazaDeveloper75/sbi-lms/blob/main/static/img/dj-lms.png?raw=true)

## Key Features
- **Simplified Password Policy**: Easy account management for students and staff.
- **Course Management**: Effortlessly handle courses, programs, and student enrollments.
- **Role-Based Access**: Specialized dashboards for Students, Teacher Instructors, and Administrators.
- **Reporting & Assessment**: Integrated quiz system and result tracking.
- **Responsive Design**: Fully optimized for mobile and desktop views.

## Quick Start (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/AliRazaDeveloper75/sbi-lms.git
cd sbi-lms
```

### 2. Set up virtual environment
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations and start server
```bash
python manage.py migrate
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` to see the app in action!

## Deployment
For instructions on how to deploy this project to **AWS EC2**, please refer to the detailed **[Deployment Guide](https://github.com/AliRazaDeveloper75/sbi-lms/blob/main/.gemini/antigravity/brain/cfba0d77-dcb7-407c-a285-1822fabed436/deployment_guide.md)**.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Developed by **Ali Raza** & Team.
```
