class App:
    def __init__(self, user_sevice, io):
        self.user_sevice = user_sevice
        self.io = io

    def run(self):
        while True:
            command = self.io.read("Command (new or login): ")

            if not command:
                break

            if command == "new":
                (username, password) = self._read_credentials()
                if len(username)>2:
                    if username.isalpha():
                        if len(password)>=8:
                            if not password.isalpha():
                                try:
                                    self.user_sevice.create_user(username, password)
                                    self.io.write("New user registered")
                                except Exception as error:
                                    self.io.write(str(error))
                            else:
                                self.io.write("Password must contain atleast one number or special character")
                        else:
                            self.io.write("Password must be at least 8 characters long")
                    else:
                        self.io.write("Username must contain only letters from alphabet")
                else:
                    self.io.write("Username must be at least 3 characters long")
            elif command == "login":
                (username, password) = self._read_credentials()

                try:
                    self.user_sevice.check_credentials(username, password)
                    self.io.write("Logged in")
                except Exception as error:
                    self.io.write(str(error))

    def _read_credentials(self):
        username = self.io.read("Username: ")
        password = self.io.read("Password: ")

        return (username, password)
