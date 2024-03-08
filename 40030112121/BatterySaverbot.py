import os
import pyttsx3


class BatterySaverBot:
    def __init__(self):
        self._moves = []
        self.places = []
        self.engine = pyttsx3.init()

    def find_path(self, origin_i, origin_j, destination_i, destination_j):
        if origin_i == destination_i and origin_j == destination_j:
            print("Error")
            return

        while origin_j > destination_j:
            self._moves.append("UP")
            origin_j -= 1
            self.places.append([origin_j, origin_i])

        while origin_j < destination_j:
            self._moves.append("DOWN")
            origin_j += 1
            self.places.append([origin_j, origin_i])

        while origin_i < destination_i:
            self._moves.append("RIGHT")
            origin_i += 1
            self.places.append([origin_j, origin_i])


        while origin_i > destination_i:
            self._moves.append("LEFT")
            origin_i -= 1
            self.places.append([origin_j, origin_i])

    def find_number_of_files(self):
        # Save the current working directory
        original_dir = os.getcwd()

        try:
            # Change to the desired directory (assuming "public" is a subdirectory)
            public_dir = os.path.join(original_dir, 'public')
            os.chdir(public_dir)

            # Get a list of all files in the folder (excluding subdirectories)
            file_list = [f for f in os.listdir(public_dir) if os.path.isfile(os.path.join(public_dir, f))]

            # Count the number of text files (assuming they have a .txt extension)
            text_file_count = len([f for f in file_list if f.lower().endswith('.txt')])

            return text_file_count

        finally:
            # Change back to the original directory
            os.chdir(original_dir)

    def print_moves(self):
        my_file = open(f"public/{self.find_number_of_files()+1}.txt", 'w')
        for i in range(len(self._moves)):
            print(self._moves[i])
            if i < len(self._moves) - 1:
                my_file.write(self._moves[i]+"_")
            else:
                my_file.write(self._moves[i])
        my_file.close()
        self.read_last_file()

    def speak(self, word):
        self.engine.say(str(word))
        self.engine.runAndWait()

    def read_last_file(self):
        src = open(f"public/{self.find_number_of_files()}.txt", "r")
        path = src.readline()
        paths = str(path.split("_")).lower()
        self.speak(paths)
