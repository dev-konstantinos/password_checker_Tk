import tkinter as tk
from tkinter import font, messagebox

def main_program(): # Hauptfunktion, die nach erfolgreichem Passwort-Check ausgeführt wird
    pass

# Neues Fenster für das Zurücksetzen des Passworts
class ResetPasswordWindow:
    def __init__(self, master, on_password_reset):
        self.master = master
        self.on_password_reset = on_password_reset

        self.window = tk.Toplevel(master)
        self.window.title("Passwort zurücksetzen")
        self.setup_geometry()
        self.create_widgets()

    def setup_geometry(self):
        window_width = 300
        window_height = 200
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        pos_top = (screen_height // 2) - (window_height // 2)
        pos_left = (screen_width // 2) - (window_width // 2)
        self.window.geometry(f"{window_width}x{window_height}+{pos_left}+{pos_top}")
        self.window.resizable(False, False)

    def create_widgets(self):
        self.secret_question_label = tk.Label(self.window, text="Was ist Ihr Geburtsort?", font=("Arial", 12))
        self.secret_question_label.pack(pady=10)

        self.secret_answer_var = tk.StringVar()
        self.secret_answer_entry = tk.Entry(self.window, textvariable=self.secret_answer_var, font=("Arial", 12))
        self.secret_answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.window, text="Antwort einreichen", command=self.reset_password)
        self.submit_button.pack(pady=10)

    def reset_password(self):
        secret_answer = self.secret_answer_var.get()
        if secret_answer == "Berlin":
            new_password = "12345"
            self.on_password_reset(new_password)
            messagebox.showinfo("Erfolg", f"Passwort zurückgesetzt! Neues Passwort: {new_password}")
            self.window.destroy()
        else:
            messagebox.showerror("Fehler", "Falsche Antwort auf die geheime Frage.")

# Neues Fenster zum Ändern des Passworts
class ChangePasswordWindow:
    def __init__(self, master, correct_password, on_password_change):
        self.master = master
        self.correct_password = correct_password
        self.on_password_change = on_password_change

        self.window = tk.Toplevel(master)
        self.window.title("Passwort ändern")
        self.setup_geometry()
        self.create_widgets()

    def setup_geometry(self):
        window_width = 300
        window_height = 240
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        pos_top = (screen_height // 2) - (window_height // 2)
        pos_left = (screen_width // 2) - (window_width // 2)
        self.window.geometry(f"{window_width}x{window_height}+{pos_left}+{pos_top}")
        self.window.resizable(False, False)

    def create_widgets(self):

        self.old_password_label = tk.Label(self.window, text="Altes Passwort:", font=("Arial", 12))
        self.old_password_label.pack(pady=5)
        self.old_password_var = tk.StringVar()
        self.old_password_entry = tk.Entry(self.window, textvariable=self.old_password_var, show="*")
        self.old_password_entry.pack(pady=5)

        self.new_password_label = tk.Label(self.window, text="Neues Passwort:", font=("Arial", 12))
        self.new_password_label.pack(pady=5)
        self.new_password_var = tk.StringVar()
        self.new_password_entry = tk.Entry(self.window, textvariable=self.new_password_var, show="*")
        self.new_password_entry.pack(pady=5)

        self.confirm_password_label = tk.Label(self.window, text="Bestätigen Sie das Passwort:", font=("Arial", 12))
        self.confirm_password_label.pack(pady=5)
        self.confirm_password_var = tk.StringVar()
        self.confirm_password_entry = tk.Entry(self.window, textvariable=self.confirm_password_var, show="*")
        self.confirm_password_entry.pack(pady=5)

        self.submit_button = tk.Button(self.window, text="Speichern", font=("Arial", 12), command=self.process_password_change)
        self.submit_button.pack(pady=10)

    def process_password_change(self):
        old_password = self.old_password_var.get()
        new_password = self.new_password_var.get()
        confirm_password = self.confirm_password_var.get()

        if old_password != self.correct_password:
            messagebox.showerror("Fehler", "Das eingegebene alte Passwort ist falsch.")
        elif new_password != confirm_password:
            messagebox.showerror("Fehler", "Die neuen Passwörter stimmen nicht überein.")
        else:
            self.on_password_change(new_password)
            messagebox.showinfo("Erfolg", "Passwort erfolgreich geändert!")
            self.window.destroy()

# Hauptklasse
class PasswordApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PASS")
        self.setup_geometry()
        self.create_fonts()
        self.correct_password = "12345"
        self.create_widgets()
        self.root.mainloop()

    def setup_geometry(self):
        window_width = 200
        window_height = 220
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        pos_top = (screen_height // 2) - (window_height // 2)
        pos_left = (screen_width // 2) - (window_width // 2)
        self.root.geometry(f"{window_width}x{window_height}+{pos_left}+{pos_top}")
        self.root.resizable(False, False)

    def create_fonts(self):
        self.small_font = font.Font(family="Arial", size=10)

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Geben Sie Ihr Passwort ein:", font=("Arial", 10, "bold"))
        self.label.pack(pady=5)

        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(self.root, textvariable=self.password_var, show="*", font=self.small_font)
        self.password_entry.pack(pady=5)

        self.password_entry.bind("<Return>", lambda event: self.check_password())
        self.submit_button = tk.Button(self.root, text="Einreichen", font=("Arial", 10, "bold"), command=self.check_password)
        self.submit_button.pack(side="top", pady=5)

        self.change_button = tk.Button(self.root, text="Ändern", font=self.small_font, command=self.open_change_password_window)
        self.change_button.pack(side="top", pady=5)

        self.reset_button = tk.Button(self.root, text="Zurücksetzen", font=self.small_font, command=self.open_reset_password_window)
        self.reset_button.pack(side="top", pady=5)

        self.quit_button = tk.Button(self.root, text="Beenden", font=self.small_font, command=self.root.quit)
        self.quit_button.pack(side="top", pady=5)

    def check_password(self):
        entered_password = self.password_var.get()
        if entered_password == self.correct_password:
            messagebox.showinfo("Erfolg", "Passwort ist korrekt! Willkommen im Programm.")
            self.root.destroy()
            main_program()  # Aufruf der Hauptfunktion bei erfolgreichem Login
        else:
            messagebox.showerror("Fehler", "Falsches Passwort. Bitte versuchen Sie es erneut.")
            self.password_var.set("")

    def open_reset_password_window(self):
        ResetPasswordWindow(self.root, self.update_password)

    def open_change_password_window(self):
        ChangePasswordWindow(self.root, self.correct_password, self.update_password)

    def update_password(self, new_password):
        self.correct_password = new_password


if __name__ == "__main__":
    PasswordApp()
