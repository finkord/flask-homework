# Example Dashboard Application


This is an example of dashboard application that organizes useful links into groups. The backend is based on Flask and frontend is served by Nginx.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/arkma/dashboard-headless.git
    cd dashboard-headless
    ```

2. **Generate initial database data:**
    ```sh
    flask --app backend/dashboard init-db
    ```

3. **Build the containers:**
    ```sh
    docker-compose build
    ```
4. **Start the app:**
    ```sh
    docker-compose up
    ```

3. **Open the app in your browser:**
    ```
    http://127.0.0.1:80
    ```
