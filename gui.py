import tkinter as tk
import os

def capture():
    os.system("python capture.py")

def train():
    os.system("python main.py")

def recognize():
    os.system("python attendanceProject.py")

def report():
    os.system("python report.py")

root = tk.Tk()
root.title("Face Recognition Attendance System")
root.geometry("400x400")

tk.Label(root, text="Attendance System", font=("Arial", 18)).pack(pady=20)

tk.Button(root, text="📸 Capture Images", command=capture, width=25).pack(pady=10)
tk.Button(root, text="🧠 Train Model", command=train, width=25).pack(pady=10)
tk.Button(root, text="👥 Start Attendance", command=recognize, width=25).pack(pady=10)
tk.Button(root, text="📊 Generate Report", command=report, width=25).pack(pady=10)

root.mainloop()