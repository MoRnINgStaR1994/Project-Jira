# Project - JIRA API Clone

A feature-rich project management API inspired by JIRA, designed to manage tasks, boards, projects and users efficiently.

## Features

- **User Management**: User registration and authentication using JWT tokens.
- **Project Management**: Create, edit, delete, list and view projects.
- **Board Management**: Manage project boards with customizable columns.
- **Ticket Management**: Add, edit, Delete, list and track tickets within boards.
- **PostgreSQL Database**: Persistent data storage for projects, boards, and tickets.
- **FastAPI**: A modern and fast Python web framework for building APIs.

---

## Tech Stack

- **Python**: v3.12.x
- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Database Driver**: psycopg2 with `RealDictCursor`
- **Authentication**: JWT, You can download it [here](https://pypi.org/project/jwt/).
- **Containerization**: Docker
- **Other Libraries**:
  - `pydantic` for data validation
  - `json` for handling JSON data

---

## Getting Started

### Prerequisites

1. **Docker**: Ensure Docker is installed on your machine. You can download it [here](https://www.docker.com/).
2. **PostgreSQL**: If you're not using the Dockerized setup, ensure PostgreSQL is installed and running. [here](https://www.kamatera.com/services/postgresql/?tcampaign=35053_474987&bta=35053&campaign=googleppc&gad_source=1&gbraid=0AAAAADiRkIC0VisAi6zh9n_J25PgfSnB0&nci=5692&scampaign=PostgreSQL).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-jira.git
   cd project-jira
   

# Project - Jira API

A project management application inspired by Jira, built using FastAPI and PostgreSQL, running in Docker.

## Start the Application

1. Update `.env` file with your credentials
2. Start Python Server:

   ```bash
   uvicorn main:app --reload
   ```
3. The application will be available at:
   - **API**: [http://localhost:8000](http://localhost:8000)
   - **Database**: `localhost:5432`

## API Endpoints

### Authentication
- **Register**: `POST /users/register`
- **Login**: `POST /users/login`
- **Refresh Access Token**: `POST /users/refresh`

### Projects
- **Create Project**: `POST /project/create`
- **Edit Project**: `POST /project/edit/{id}`
- **Delete Project**: `DELETE /project/{id}`
- **List User Projects**: `GET /project`

### Boards
- **Create Board**: `POST /project/board/create`
- **Edit Board**: `POST /project/board/edit/{id}`
- **Delete Board**: `DELETE /project/board/delete/{id}`
- **Get Board Details**: `GET /project/board/details/{id}`

### Tickets
- **Create Ticket**: `POST /ticket/create`
- **Edit Ticket**: `POST /ticket/edit/{id}`
- **Delete Ticket**: `DELETE /ticket/{id}`
- **Get Board Tickets**: `GET /ticket/details/{id}`

## Project Structure

```
project-jira/
├── app/
│   ├── models/
│   │   ├── Project.py
│   │   ├── Board.py
│   │   ├── Ticket.py
│   │   └── Person.py
│   ├── repositories/
│   │   └── conn/
│   │   ├   └── get_connection.py
│   │   ├── PersonRepository.py
│   │   ├── ProjectRepository.py
│   │   ├── TicketRepository.py
│   ├── routes/
│   │   ├── person.py
│   │   └── project.py
│   │   ├── ticket.py
│   ├── schemas/
│   │   └── person.py
│   │   ├── project.py
│   │   ├── ticket.py
│   ├── services/
│   │   ├── PersonService.py
│   │   ├── ProjectService.py
│   │   ├── TicketService.py
│   ├── dbengine.py
│   ├── rsa_private_key.pem
│   ├── rsa_public_key.pem
│   ├── utils.py
├── requirements.txt
├── .gitignore
├── main.py
└── readme.md
```

## Contact
For support or inquiries, contact [datokamadadze12@gmail.com](mailto:your-email@example.com)

