class Server:
    def __init__(self, hostname, status, cpu_usage):
        self.hostname = hostname
        self.status = status
        self.cpu_usage = cpu_usage  

    def boot(self):
        self.status = "Running"

    def shutdown(self):
        self.status = "Off"

    def increase_load(self):
        self.cpu_usage += 10

    def display_status(self):
        print(self.hostname, self.status, self.cpu_usage)

server = Server("server-01", "Off", 0)
server.boot()
server.display_status()