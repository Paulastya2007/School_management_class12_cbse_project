### Project Setup

#### Container Environment
**Prerequisites:** Docker Compose

1. **Start the container:**
   ```bash
   docker-compose up -d
   ```
   This will start a container with the MySQL database.

2. **Access the MySQL container:**
   * Find the container ID:
     ```bash
     docker ps
     ```
   * Access the MySQL console:
     ```bash
     docker exec -it <container_id> mysql -u root -pmy-secret-pw
     ```
   * Create database and tables (if not already created):
     ```sql
     SOURCE /SQL/database_setup.sql
     SOURCE /SQL/Dummy_Values.sql
     ```

**Note:** Replace `my-secret-pw` with your actual MySQL root password.

#### Local Machine (Windows or Linux)



**Prerequisites:** Python 3, pip

1. **Create a virtual environment:**
   ```bash
   python3 -m venv myenv
   ```
   ```bash
   source myenv/bin/activate  # Linux
   ```
   ```bash
   myenv\Scripts\activate  # Windows
   ```
2. **Install required packages:**
   ```bash
   pip install mysql-connector-python pandas
   ```

### Database Connection
**Replace placeholders with your actual credentials: in main.py**
```python
import mysql.connector

db = mysql.connector.connect(
    user='root',
    password='your_password',
    host='localhost',  # For local machine
    database='your_database_name'
)
```

### Using GitHub Codespaces
**Note:** Ensure you have a `.devcontainer` file set up correctly for your project in GitHub Codespaces.

**1. Open the project in Codespaces:**
   * Fork or clone the repository to your GitHub account.
   * Open the project in Codespaces.

**2. Follow the container environment setup steps above.**
   * The `.devcontainer` file should handle the necessary Docker Compose setup.

### Using Local Machine
**1. Clone the repository:**
   ```bash
   gh repo clone Paulastya2007/School_management_class12_cbse_project
   ```
**2. Follow the local machine setup steps above.**

