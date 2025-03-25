### Task Management API - Django & DRF

A simple **Task Management API** built using Django & Django Rest Framework that allows users to:
- **Create Tasks**
- **Assign Tasks to Users**
- **Retrieve Tasks Assigned to a User**

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/MohamamdAzam/Task_Management_Josh_Talk.git
cd Task_Management_Josh_Talk
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv venv # On Windows: virtualenv env
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database & Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```
_Follow the prompts to set up an admin user._

### 6. Run the Server
```bash
python manage.py runserver
```
_Server will start at: **http://127.0.0.1:8000/**_

---

## 🔦 API Endpoints & Usage

### 1⃣ Create a User
**Endpoint:**
```http
POST /api/users/create/
```
**Request Body:**
```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "mobile": "1234567890"
}
```
**Response:**
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "mobile": "1234567890"
}
```

---

### 2⃣ Create a Task
**Endpoint:**
```http
POST /api/tasks/create/
```
**Request Body:**
```json
{
    "name": "Complete Report",
    "description": "Prepare and submit the quarterly report."
}
```
**Response:**
```json
{
    "id": 1,
    "name": "Complete Report",
    "description": "Prepare and submit the quarterly report.",
    "created_at": "2025-03-24T12:00:00Z",
    "status": "pending"
}
```

---

### 3⃣ Assign a Task to Users
**Endpoint:**
```http
POST /api/tasks/{task_id}/assign/
```
**Request Body:**
```json
{
    "assigned_users": [1]
}
```
**Response:**
```json
{
    "message": "Users assigned successfully."
}
```

---

### 4⃣ Get Tasks for a Specific User
**Endpoint:**
```http
GET /api/users/{user_id}/tasks/
```
**Response:**
```json
[
    {
        "id": 1,
        "name": "Complete Report",
        "description": "Prepare and submit the quarterly report.",
        "status": "pending",
        "assigned_users": [
            {
                "id": 1,
                "name": "John Doe"
            }
        ]
    }
]
```


---

## 💜 Notes
- The API follows **RESTful principles** and returns JSON responses.
- Make sure your database is properly migrated before running the server.
- You can use **Postman** or **cURL** to test the API endpoints.

---

## 📌 License
This project is open-source under the **MIT License**.

