# 🚀 SpaceHub

> A Django-based co-working space booking platform built as a comprehensive training project covering authentication, authorization, ORM relationships, transactions, and more.

---

## 📌 Project Info

| | |
|---|---|
| **Project Name** | SpaceHub |
| **Description** | A co-working space booking platform where Owners can list their spaces and Tenants can browse, filter, and book them. Built with Django, covering authentication, authorization, ORM relationships, transactions, pagination, media files, and Django Admin. |
| **User Stories** | 📄 [View User Stories](docs/SpaceHub_User_Stories.pdf) |
| **UML Diagram** | 📊 [View UML](docs/SpaceHub_UML_.pdf) |
| **Wireframe** | 🖼️ [View Wireframe](<docs/SpaceHub_wireframe.pdf) |

---

## ✅ Features

- User registration and login with two roles: **Owner** and **Tenant**
- Role-based access control using Django Groups and Permissions
- Owners can add, edit, and manage their own spaces
- Tenants can browse, search, filter, and book spaces
- Space listings with images, type, and availability status
- Booking system with atomic transactions
- Reviews and star ratings per space
- Average rating aggregation and booking count per space
- Pagination (6 spaces per page)
- Flash messages for user feedback (success / error / warning)
- Media file uploads for space images via Cloudinary / Firebase
- Fully responsive design using a CSS library
- Django Admin panel with filters and display customization
- Environment variables managed with `python-dotenv`

---

## 📋 Table of Contents

- [About](#about)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Apps Overview](#apps-overview)
- [Sessions Covered](#sessions-covered)
- [URL Routes](#url-routes)
- [Getting Started](#getting-started)

---

## About

**SpaceHub** is a training Django project that simulates a real-world co-working space booking system. It is designed to cover essential Django concepts across 13 sessions — from authentication and authorization to advanced ORM queries, media files, pagination, and Django Admin.

The platform supports two user roles:
- **Owner** — can add and manage their own spaces
- **Tenant** — can browse and book available spaces

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django (Python) |
| Database | SQLite (development) |
| Image Handling | Pillow |
| Frontend | Django Templates |

---

## Project Structure

```
spacehub/
│
├── accounts/         # Authentication, Authorization, Groups
├── spaces/           # Space listings, images, field choices
├── bookings/         # Reservations, transactions
├── reviews/          # Ratings, aggregates
│
├── media/            # Uploaded space images
├── static/           # Static files
├── templates/        # HTML templates
│
├── spacehub/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

---

## Apps Overview

### `accounts`
Handles everything related to users:
- Register / Login / Logout
- User roles via Django Groups (`Owner`, `Tenant`)
- Permissions and `has_perm` checks
- `OneToOne` Profile linked to User

### `spaces`
Manages co-working space listings:
- Space model with `ForeignKey` to User (Owner)
- `ManyToMany` relationship with Amenities
- `ImageField` with Pillow for space photos
- `TextChoices` / `IntegerChoices` for space type and status
- Pagination (6 spaces per page)

### `bookings`
Handles the reservation flow:
- Booking model with status `Choices`
- `transaction.atomic()` when creating a booking
- `on_commit` for post-transaction actions
- Flash messages (success / error / warning)

### `reviews`
Manages tenant reviews and ratings:
- Review model linked to Space and Tenant
- `aggregate()` for average rating
- `annotate()` for booking count per space

---

## Sessions Covered

| # | Session | Where It Appears in SpaceHub |
|---|---|---|
| 1 | Authentication | Register as Owner or Tenant, Login, Logout |
| 2 | Authorization | Owner edits own spaces only — Tenant books only |
| 3 | Groups | `user.groups.add(group)` on registration |
| 4 | Django ORM | All models, CRUD operations, field types |
| 5 | ORM Relationships | `Space→User (FK)`, `Profile→User (OneToOne)`, `M2M Amenities` |
| 6 | ORM Relations | `related_name`, `spaces__city` filtering, `prefetch_related` |
| 7 | Advanced ORM | `Q` for search, `aggregate` for ratings, `annotate` for booking count |
| 8 | Field Choices | Space type and booking status using `TextChoices` |
| 9 | Transactions | `transaction.atomic()` when creating a booking |
| 10 | Pagination | Space list — 6 spaces per page |
| 11 | Messages | Booking confirmation and error flash messages |
| 12 | Media Files | Space image upload via `ImageField` + `MEDIA_URL` |
| 13 | Django Admin | `list_display`, `list_filter` for all models |

---

## URL Routes

| URL | Description | Access |
|---|---|---|
| `/` | Home — search, filter, display spaces | Public |
| `/spaces/` | Space list with pagination | Public |
| `/spaces/<id>/` | Space detail + booking form | Tenant |
| `/spaces/add/` | Add a new space | Owner only |
| `/owner/dashboard/` | Owner dashboard | Owner only |
| `/tenant/dashboard/` | Tenant dashboard | Tenant only |
| `/accounts/register/` | User registration | Public |
| `/accounts/login/` | User login | Public |
| `/accounts/logout/` | User logout | Authenticated |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/spacehub.git
cd spacehub
```

### 2. Create a virtual environment

```bash
py -m venv env
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django pillow
```

### 4. Apply migrations

```bash
py manage.py makemigrations
py manage.py migrate
```

### 5. Create a superuser

```bash
py manage.py createsuperuser
```

### 6. Run the server

```bash
py manage.py runserver
```

Open your browser at: `http://127.0.0.1:8000/`

---

> Built with 💙 as part of a Django training program.