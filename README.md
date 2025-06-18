# 🧩 TeamTracker – Role-Based Task & Project Management Platform

TeamTracker is a **Dockerized Django** application for managing tasks and projects within an organization, with **role-based access control** for Admins, Managers, and Members.

🚀 Built for team collaboration and streamlined workflow management, TeamTracker is a scalable, production-ready backend platform.

---

## 🔧 Tech Stack

- **Backend:** Django, PostgreSQL
- **Auth:** Django Custom User Model with Roles (Admin, Manager, Member)
- **DevOps:** Docker, Docker Compose
- **Deployment Ready:** Gunicorn + PostgreSQL in containers
- **Frontend:** HTML (basic), Bootstrap (optional)
- **Others:** ORM, Admin Panel, Role-Based Views

---

## 📸 Features

- 🧑‍💼 **Role-based dashboards** (Admin, Manager, Member)
- 📁 **Project and Task Management** with ownership and deadlines
- 🔒 **User Registration/Login** with secure password hashing
- 📦 **Dockerized** for local and cloud deployment
- 🧠 **Custom user roles** using Django’s AbstractUser
- 🔧 **PostgreSQL database** with Docker volume persistence

---
## 📂 Folder Structure

```bash
TeamTrack/
├── core/               # App with views, models, forms
├── taskflow/           # Project root with settings
├── templates/          # HTML templates
├── Dockerfile          # Container for web service
├── docker-compose.yml  # Runs web + db
├── requirements.txt    # Python dependencies
└── .env                # Environment variables (excluded from Git)
```
---
## 📸 Features Overview

### 🔐 Authentication & Roles
- Custom roles: **Admin**, **Manager**, **Member**
- Role-based dashboards and permissions

### 🧑‍💼 Admin Dashboard
- Manage all users, projects, and tasks
- Assign users and define roles

### 📁 Project Management
- Create/edit/delete projects
- Assign managers or team members

### 📌 Task Management
- Create/edit/delete tasks
- Assign to users, set priority, deadline, and status

### 📊 Member View
- Access assigned tasks only
- Update task progress/status

---



