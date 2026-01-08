# 📝 Flask Task Manager Application

A simple, elegant, and practical task management web application built with Flask. This project demonstrates real-life implementation of a web application with CRUD operations, routing, and templating.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

- ✅ **Add Tasks**: Create new tasks with a single click
- ✓ **Complete Tasks**: Mark tasks as completed
- ✗ **Delete Tasks**: Remove tasks from your list
- 📊 **Statistics Dashboard**: View total, pending, and completed tasks
- 🎨 **Beautiful UI**: Modern gradient design with smooth animations
- 📱 **Responsive Design**: Works on desktop and mobile devices

## 🖼️ Screenshots

### Home Page
![Home Page](screenshot.png)
*Main interface showing task list with statistics*

### Application Running
![Terminal Output](terminal_screenshot.png)
*Flask application running in terminal*

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayanatiq01-arch/parallel-DC.git
   cd parallel-DC/chap7
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to: `http://localhost:5000`

## 📂 Project Structure

```
chap7/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── CONCLUSION.md         # Project conclusion and learnings
├── screenshot.png        # Application screenshot
├── terminal_screenshot.png # Terminal output screenshot
│
└── templates/
    ├── index.html        # Home page template
    └── about.html        # About page template
```

## 🛠️ Technology Stack

- **Backend Framework**: Flask 3.0.0
- **Templating Engine**: Jinja2
- **Frontend**: HTML5, CSS3
- **Server**: Werkzeug 3.0.1 (development server)

## 📖 How It Works

### Routes

- **`/`** - Home page displaying all tasks
- **`/add`** (POST) - Add a new task
- **`/complete/<task_id>`** - Mark a task as completed
- **`/delete/<task_id>`** - Delete a task
- **`/about`** - About page with application information

### Data Structure

Tasks are stored in memory with the following structure:
```python
{
    "id": 1,
    "title": "Task name",
    "completed": False,
    "created": "2026-01-07"
}
```

## 💡 Usage Examples

### Adding a Task
1. Enter your task in the input field
2. Click "Add Task" button
3. Task appears in the list below

### Completing a Task
1. Click the "✓ Complete" button next to any pending task
2. Task is marked as completed with a strikethrough

### Deleting a Task
1. Click the "✗ Delete" button next to any task
2. Task is removed from the list

## 🎯 Learning Objectives

This project demonstrates:
- Flask routing and request handling
- Template rendering with Jinja2
- Form processing and data manipulation
- Responsive web design with CSS
- RESTful URL patterns
- Basic CRUD operations

## 🔧 Configuration

The application runs with the following default settings:
- **Host**: 0.0.0.0 (accessible from all network interfaces)
- **Port**: 5000
- **Debug Mode**: Enabled (disable in production)

## 📝 Notes

- This application uses in-memory storage. All data is lost when the server restarts.
- For production use, consider implementing a database (SQLite, PostgreSQL, etc.)
- Debug mode should be disabled in production environments

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

**Parallel-DC Project**
- GitHub: [@ayanatiq01-arch](https://github.com/ayanatiq01-arch)
- Repository: [parallel-DC](https://github.com/ayanatiq01-arch/parallel-DC)

## 🙏 Acknowledgments

- Flask documentation and community
- Modern web design inspiration
- Python community for excellent tools and libraries

---

**Happy Task Managing! 🎉**

For more details, see [CONCLUSION.md](CONCLUSION.md)
