# TBR Carousel

TBR Carousel is a personalized web app that helps readers manage their book collections and pick their next read using a fun spinning wheel.  
Designed to make reading more playful and less overwhelming, it lets users organize books, apply filters, and spin a digital carousel for random recommendations.

---

## Features

- User authentication (sign up, login, logout)
- Personal library: add, edit, delete books
- Smart filters: mood, genre, length, author
- Interactive spinning carousel to pick a book
- Reading status tracker (To Read, Reading, Read, DNF)
- Google Books API autofill for book details
- Flash messages for user feedback

---

## Tech Stack

- **Backend:** Python, Flask, Flask-Login, Flask-WTF, SQLAlchemy, Flask-Migrate
- **Frontend:** HTML, CSS, JavaScript (vanilla), Bootstrap, Jinja2
- **Database:** SQLite
- **API:** Google Books API
- **Containerized with:** Docker

---

## Run with Docker

Make sure Docker Desktop is installed and running.

```bash
# Clone the repository
git clone https://github.com/Nata-Bobokhidze/TBR.git
cd TBR

# Build the Docker image
docker build -t tbr-carousel .

# Run the app
docker run -p 5000:5000 tbr-carousel

Visit http://localhost:5000 in your browser.
```

## Project Structure
TBR/
├── app/              # Factory app package
├── auth/             # Authentication blueprint
├── books/            # Book routes & logic
├── carousel/         # Carousel routes & filtering
├── core/             # Main routes (dashboard, welcome)
├── static/           # JS, CSS
├── templates/        # Jinja2 HTML templates
├── run.py            # Main entry point
├── Dockerfile        # For Docker builds
├── requirements.txt  # Dependencies
└── README.md         # This file

## Author

**Nata Bobokhidze**  
[GitHub Profile](https://github.com/Nata-Bobokhidze)
