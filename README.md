# Student-DB-Docker-App
A simple hands-on project to understand how 2-tier architecture works using Docker. 


### Setup
1. Clone the repo.
2. Run `docker-compose up --build`.
3. The app will prompt you to enter student details.

### My Learnings
- Containerizing a Python app.
- Linking a DB container with an App container via Docker Network.
- Using Docker Volumes for data persistence (so my data doesn't disappear).

## Commands used:
- Build: `docker build -t student-app .`
- Up: `docker-compose up`