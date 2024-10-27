import tkinter as tk
import threading
import time


class Klijent:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.root.title("Klijentska strana")

        # Header sekcija
        self.header = tk.Frame(root, width=800, height=50, bg="lightgrey")
        self.header.pack_propagate(False)
        self.header.pack()

        # Canvas za crtanje polukruga
        self.canvas = tk.Canvas(self.header, width=800, height=50, bg="lightgrey")
        self.canvas.pack()

        # Footer sekcija
        self.footer = tk.Frame(root, width=800, height=50, bg="lightgrey")
        self.footer.pack_propagate(False)
        self.footer.pack(side=tk.BOTTOM)

        # Ispis u footeru
        footer_label = tk.Label(self.footer, text="© 2024 Mladjan Matejic MIN-19/23, Igor Kuburovic RIN-50/23", bg="lightgrey")
        footer_label.pack(pady=15)  # Povećajte prostor oko teksta

        # Pokretanje niti za animaciju polukruga
        self.running = True
        self.circle_thread = threading.Thread(target=self.animate_semicircle)
        self.circle_thread.start()

    def animate_semicircle(self):
        # Parametri za animaciju
        start_angle = 0
        end_angle = 180
        angle_step = 10  # Korak u stepenima za iscrtavanje

        while self.running:
            # Punjenje polukruga s desne ka levoj strani
            for angle in range(0, 181, angle_step):
                self.canvas.delete("semicircle")
                self.canvas.create_arc(360, 10, 440, 90, start=start_angle, extent=angle, fill="blue",
                                       tags="semicircle")
                time.sleep(0.05)  # Pauza za animaciju

            # Pražnjenje polukruga
            for angle in range(180, -1, -angle_step):
                self.canvas.delete("semicircle")
                self.canvas.create_arc(360, 10, 440, 90, start=start_angle, extent=angle, fill="blue",
                                       tags="semicircle")
                time.sleep(0.05)  # Pauza za animaciju

    def on_close(self):
        # Zaustavljanje animacije i zatvaranje prozora
        self.running = False
        self.circle_thread.join()
        self.root.destroy()


# Pokretanje klijentske strane
if __name__ == "__main__":
    root = tk.Tk()
    app = Klijent(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
