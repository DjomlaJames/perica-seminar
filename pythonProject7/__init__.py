# __init__.py - Serverska strana
import tkinter as tk
import socket
import pymysql
import threading


class Server:
    def __init__(self, root):
        self.root = root
        self.root.geometry("100x800")
        self.root.title("Serverska strana")

        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # Start server in a separate thread to allow Tkinter GUI to remain responsive
        self.server_thread = threading.Thread(target=self.start_server)
        self.server_thread.start()

    def start_server(self):
        # Setting up server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(5)

        self.listbox.insert(tk.END, "Server pokrenut i ceka veze...")

        while True:
            client_socket, addr = server_socket.accept()
            self.listbox.insert(tk.END, f"Klijent povezan: {addr}")
            # Add logic here to handle client requests

    def db_interaction(self, query):
        # Database interaction example
        connection = pymysql.connect(host='localhost', user='root', password='password', database='baza01')
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result

    def on_close(self):
        # Close the application and any necessary cleanup
        self.root.destroy()


# Running the server GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = Server(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
