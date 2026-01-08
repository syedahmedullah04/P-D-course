# 🚀 Quick Start Guide

## Step-by-Step Instructions to Run the Application

### Step 1: Install Flask
Open Command Prompt or PowerShell in the chap7 folder and run:
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

You should see output like:
```
==================================================
🚀 Task Manager Application Starting...
==================================================
📝 Access the application at: http://localhost:5000
📊 Features: Add, Complete, and Delete Tasks
==================================================
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.x.x:5000
Press CTRL+C to quit
```

### Step 3: Open in Browser
1. Open your web browser
2. Go to: `http://localhost:5000`
3. You should see the Task Manager interface!

### Step 4: Test the Application
1. **Add a task**: Type something in the input field and click "Add Task"
2. **Complete a task**: Click the "✓ Complete" button
3. **Delete a task**: Click the "✗ Delete" button
4. **View About page**: Click the "About" link at the bottom

### Step 5: Take Screenshots
Follow the instructions in `SCREENSHOT_GUIDE.md` to capture:
1. The application interface (save as `screenshot.png`)
2. The terminal output (save as `terminal_screenshot.png`)

### Step 6: Stop the Server
Press `Ctrl + C` in the terminal to stop the Flask server.

## 📤 Uploading to GitHub

### If you haven't initialized git yet:
```bash
cd c:\Users\Dell\Desktop\parallel-DC\chap7
git add .
git commit -m "Add Flask Task Manager application with documentation"
git push origin main
```

### If this is a new folder in existing repo:
```bash
git add chap7/
git commit -m "Add Chapter 7: Flask Task Manager application"
git push origin main
```

## ✅ Checklist Before Uploading

- [ ] Flask installed successfully
- [ ] Application runs without errors
- [ ] Tested all features (add, complete, delete)
- [ ] Took screenshot of application (`screenshot.png`)
- [ ] Took screenshot of terminal (`terminal_screenshot.png`)
- [ ] All files present: app.py, requirements.txt, README.md, CONCLUSION.md
- [ ] Templates folder with index.html and about.html
- [ ] Ready to commit and push to GitHub

## 🆘 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Run `pip install -r requirements.txt`

### Error: "Address already in use"
**Solution**: Another program is using port 5000. Change the port in app.py:
```python
app.run(host="0.0.0.0", port=int("5001"), debug=True)
```

### Error: "Template not found"
**Solution**: Make sure the `templates` folder exists with `index.html` and `about.html`

## 🎉 Success!

Once everything is working:
1. Your application is running at http://localhost:5000
2. Screenshots are saved
3. All documentation is complete
4. Ready to push to GitHub!

Congratulations! You've successfully created and deployed a Flask web application! 🚀
