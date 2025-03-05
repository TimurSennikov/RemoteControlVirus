import customtkinter as ctk
import os

class InstallFrame(ctk.CTkFrame):
    def read_i(self):
        try:
            with open("install.txt", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return "Произошла ошибка при чтении условий установки."

    def accept(self):
        for widget in self.winfo_children():
            widget.destroy()

        progbar = ctk.CTkProgressBar(self, height=50, fg_color="#228B22", indeterminate_speed=0.1, determinate_speed=0.05)
        progbar.start()

        progbar.pack(expand=True, fill="x")

    def cancel(self):
        pass

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.conditions = ctk.CTkTextbox(self)

        self.conditions.insert("0.0", self.read_i())

        self.accept = ctk.CTkButton(self, text="Установить", command=self.accept)
        self.cancel = ctk.CTkButton(self, text="Отмена", command=self.cancel)

        self.conditions.pack(expand=True, fill="both")
        self.accept.pack(pady=5)
        self.cancel.pack(pady=5)

class InstallWindow(ctk.CTk):
    def read_p(self):
        try:
            with open("policy.txt", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return "Ошибка загрузки политики конфиденциальности"

    def process_checkbox(self):
        if self.policy_accept.get() == 1:
            self.accept.configure(state="normal")
        else:
            self.accept.configure(state="disabled")

    def process_install(self):
        for widget in self.winfo_children():
            widget.destroy()

        f = InstallFrame(master=self)
        f.pack(expand=True, fill="both")

    def process_cancel(self):
        self.destroy()
        exit()

    def __init__(self):
        super().__init__()

        self.geometry("640x480")

        self.policy = ctk.CTkTextbox(self)
        self.policy.insert("0.0", self.read_p())
        self.policy.configure(state="disabled")

        self.policy_accept = ctk.CTkCheckBox(self, text="Я прочитал и согласен(-а) с условиями лицензионного соглашения", command=self.process_checkbox)

        self.accept = ctk.CTkButton(self, text="Продолжить", state="disabled", command=self.process_install)
        self.cancel = ctk.CTkButton(self, text="Отмена", state="normal", command=self.process_cancel)

        self.policy.pack(expand=True, fill="both")
        self.policy_accept.pack()
        self.accept.pack(pady=5)
        self.cancel.pack(pady=5)