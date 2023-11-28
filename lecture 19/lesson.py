import json

"""
This program will create a file database for dog races
 """

FILE_NAME = "dog_db.json"
# Optional:
FILE_PATH = "C:/mycomputer/files/"
COMPLETE_FILE_PATH = FILE_PATH + FILE_NAME


class DogDataBase:
    def __init__(self):
        self.my_dogs = []
        self.load_data()

    def update_data(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.my_dogs, file, indent=2)

    def add_race(self, dog_race):
        self.my_dogs.append(dog_race)
        self.update_data()

    def load_data(self):
        try:
            with open(FILE_NAME, "r") as file:
                self.my_dogs = json.load(file)
                print("File succesfully loaded")
        except FileNotFoundError as e:
            print("Creating file anew")

    def get_my_dogs(self):
        return self.my_dogs


def main():
    dog_database = DogDataBase()
    dog_object = {
        "Leonberger": {"fur_thickness": "big", "size": "large", "aggressivness": "low"}
    }
    dog_object1 = {
        "Golden Retriever": {
            "fur_thickness": "medium",
            "size": "medium",
            "aggressivness": "extremely low",
        }
    }

    dog_database.add_race(dog_object)
    dog_database.add_race(dog_object1)

    my_dogs = dog_database.get_my_dogs()

    for dog_race in my_dogs:
        print(dog_race["Leonberger"])
        break


if __name__ == "__main__":
    main()
