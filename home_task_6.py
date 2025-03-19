# Import the datetime module for date and time manipulations
import datetime

# Import the os module to interact with the operating system
import os

# Import the sys module to access command-line arguments
import sys

# Import specific functions from the `home_task_4_string` module
from home_task_4_string import normalize_text, correct_iz, capitalize_sentence


# Define the NewsFeedGenerator class that handles the creation and management of a news feed
class NewsFeedGenerator:
    # Initialize the class with an optional file name argument, defaulting to "news_feed.txt"
    def __init__(self, file_name="news_feed.txt"):
        self.file_name = file_name

    # Method to read existing content from the file
    def read_existing_content(self):
        # Define a dictionary to store different sections of the news feed
        sections = {"News": [], "PrivateAd": [], "BirthAnnouncement": []}
        current_section = None

        try:
            # Attempt to open the file in read mode
            with open(self.file_name, "r") as file:
                content = file.readlines()
            # Process each line and append it to the appropriate section
            for line in content:
                if line.startswith("News-------------------"):
                    current_section = "News"
                    sections[current_section].append(line)
                elif line.startswith("Private ad-------------"):
                    current_section = "PrivateAd"
                    sections[current_section].append(line)
                elif line.startswith("Birth announcement-----"):
                    current_section = "BirthAnnouncement"
                    sections[current_section].append(line)
                elif current_section:
                    sections[current_section].append(line)
        # If the file is not found, create it with a default header
        except FileNotFoundError:
            with open(self.file_name, "w") as file:
                file.write("News feed:\n\n")
            print(f"File {self.file_name} created with default header!")
        # Handle other exceptions that may occur
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

        # Return the sections dictionary
        return sections

    # Method to write new sections to the file
    def write_to_file(self, new_sections):
        # Read the existing content from the file
        existing_sections = self.read_existing_content()

        # Append the new entries to the existing sections
        for section in new_sections:
            existing_sections[section].extend(new_sections[section])

        try:
            # Write the combined content back to the file
            with open(self.file_name, "w") as file:
                file.write("News feed:\n\n")
                for section in ["News", "PrivateAd", "BirthAnnouncement"]:
                    for entry in existing_sections[section]:
                        file.write(entry)
            print("Records updated in the file successfully!")
        # Handle any exceptions that occur during writing
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    # Method to start the generator's user interface
    def start(self):
        # Continuously present the user with options until they choose to exit
        while True:
            print("\nWould you like to:")
            print("1. Add entries manually")
            print("2. Download from a file")
            print("3. Exit")
            initial_choice = input("Enter your choice (1/2/3): ")

            # Respond to user choices by invoking appropriate methods
            if initial_choice == "1":
                self.add_manually()
            elif initial_choice == "2":
                self.import_from_file()
            elif initial_choice == "3":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2 or 3.")

    # Method to add entries manually
    def add_manually(self):
        # Continuously present the user with options until they choose to exit
        while True:
            print("\nSelect what to add:")
            print("1. News")
            print("2. Private Ad")
            print("3. Birth Announcement")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            # Respond to user choices by creating new entries and writing them to the file
            if choice == "1":
                news = News()
                entry = news.add_entry()
                sections = {"News": [entry], "PrivateAd": [], "BirthAnnouncement": []}
                self.write_to_file(sections)
            elif choice == "2":
                private_ad = PrivateAd()
                entry = private_ad.add_entry()
                sections = {"News": [], "PrivateAd": [entry], "BirthAnnouncement": []}
                self.write_to_file(sections)
            elif choice == "3":
                birth_announcement = BirthAnnouncement()
                entry = birth_announcement.add_entry()
                sections = {"News": [], "PrivateAd": [], "BirthAnnouncement": [entry]}
                self.write_to_file(sections)
            elif choice == "4":
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3 or 4.")

    # Method to import entries from a file
    def import_from_file(self):
        importer = ImportFromFile()
        # Present the user with options until they choose to exit
        while True:
            print("\nSelect file location:")
            print("1. Default folder")
            print("2. User provided file path")
            print("3. Exit")
            file_choice = input("Enter your choice (1/2/3): ")

            # Depending on the choice, import the file from the default folder or from a user-provided path
            if file_choice == "1":
                try:
                    file_path = importer.get_file_from_default_folder()
                    if file_path:
                        new_sections = importer.parse_file(file_path)
                        self.write_to_file(new_sections)
                        importer.remove_file(file_path)
                except Exception as e:
                    print(f"An error occurred during file processing or writing: {e}")
                break
            elif file_choice == "2":
                try:
                    file_path = importer.get_file_from_user_path()
                    if file_path:
                        new_sections = importer.parse_file(file_path)
                        self.write_to_file(new_sections)
                        importer.remove_file(file_path)
                except Exception as e:
                    print(f"An error occurred during file processing or writing: {e}")
                break
            elif file_choice == "3":
                print("Returning to main menu.")
                break
            else:
                print("Invalid choice. Please select 1, 2 or 3.")


# Class representing a News entry
class News:
    # Method to add a news entry
    def add_entry(self):
        while True:
            # Prompt the user for news text
            news_text = input("Enter the news text: ").strip()
            if news_text:
                break
            else:
                print("News text cannot be empty. Please enter a valid news text.")

        while True:
            # Prompt the user for the city
            city = input("Enter the city: ").strip()
            if city:
                break
            else:
                print("City cannot be empty. Please enter a valid city.")

        # Get the current date and time
        publish_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

        # Return the formatted news entry
        return (
            "News-------------------\n"
            f"Text: {capitalize_sentence(news_text.strip())}\n"
            f"City: {capitalize_sentence(city.strip())}\n"
            f"{publish_date}\n\n"
        )


# Class representing a Private Advertisement entry
class PrivateAd:
    # Method to add a private ad entry
    def add_entry(self):
        while True:
            # Prompt the user for ad text
            ad_text = input("Enter the ad text: ").strip()
            if ad_text:
                break
            else:
                print("Ad text cannot be empty. Please enter a valid ad text.")

        while True:
            # Prompt the user for the expiration date
            expiration_date = input("Enter expiration date (DD/MM/YYYY): ").strip()
            try:
                expiration_date_obj = datetime.datetime.strptime(expiration_date, "%d/%m/%Y")
                days_left = (expiration_date_obj.date() - datetime.datetime.now().date()).days

                if days_left < 0:
                    print("The expiration date has already passed. Please enter a future date.")
                elif days_left == 0:
                    print("The expiration date is today. The ad will expire at the end of the day.")
                    break
                else:
                    break
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        # Return the formatted private ad entry
        return (
            "Private ad-------------\n"
            f"Text: {capitalize_sentence(ad_text.strip())}\n"
            f"Expiration date: {expiration_date}\n"
            f"Actual until: {expiration_date}, {days_left} days left\n\n"
        )


# Class representing a Birth Announcement entry
class BirthAnnouncement:
    # Method to add a birth announcement entry
    def add_entry(self):
        while True:
            # Prompt the user for the child's name
            child_name = input("Enter the child's name: ").strip()
            if child_name:
                break
            else:
                print("Child's name cannot be empty. Please enter a valid name.")

        while True:
            # Prompt the user for the location
            location = input("Enter the location: ").strip()
            if location:
                break
            else:
                print("Location cannot be empty. Please enter a valid location.")

        while True:
            # Prompt the user for a short message
            message = input("Enter a short message about the child: ").strip()
            if message:
                break
            else:
                print("Message cannot be empty. Please enter a valid message.")

        while True:
            # Prompt the user for the birth date
            birth_date = input("Enter the birth date (DD/MM/YYYY): ").strip()
            try:
                birth_date_obj = datetime.datetime.strptime(birth_date, "%d/%m/%Y")
                if birth_date_obj > datetime.datetime.now():
                    print("Birth date cannot be in the future. Please enter a past date.")
                else:
                    break
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        # Return the formatted birth announcement entry
        return (
            "Birth announcement-----\n"
            f"Child name: {capitalize_sentence(child_name.strip())}\n"
            f"Birth date: {birth_date}\n"
            f"Location: {capitalize_sentence(location.strip())}\n"
            f"Message: {capitalize_sentence(message.strip())}\n\n"
        )


# Class to handle importing entries from a file
class ImportFromFile:
    # Initialize with a default folder name, creating the folder if it doesn't exist
    def __init__(self, default_folder="imports"):
        self.default_folder = default_folder
        if not os.path.exists(self.default_folder):
            os.makedirs(self.default_folder)

    # Method to get a file from the default folder
    def get_file_from_default_folder(self):
        files = [f for f in os.listdir(self.default_folder) if f.endswith(".txt")]
        if not files:
            print("No text files found in the default folder.")
            return None
        return os.path.join(self.default_folder, files[0])

    # Method to get a file from a user-provided path
    def get_file_from_user_path(self):
        file_path = input("Enter the file path: ").strip()
        if not os.path.isfile(file_path):
            print("Invalid file path.")
            return None
        return file_path

    # Method to parse the content of a file and categorize entries
    def parse_file(self, file_path):
        sections = {"News": [], "PrivateAd": [], "BirthAnnouncement": []}
        try:
            with open(file_path, "r") as file:
                content = file.read()

            # Normalize and correct the content text
            content = normalize_text(content)
            content = correct_iz(content)
            entries = content.split("\n\n")

            # Process each entry and format it appropriately
            for entry in entries:
                lines = entry.strip().split("\n")
                if len(lines) < 3:
                    continue

                header = lines[0].strip()
                if "news" in header.lower():
                    section = "News"
                    news_text = lines[1][6:].strip()
                    city = lines[2][5:].strip()
                    publish_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                    formatted_entry = (
                        f"News-------------------\nText: {capitalize_sentence(news_text)}\nCity: {capitalize_sentence(city)}\n{publish_date}\n\n"
                    )
                    sections["News"].append(formatted_entry)
                elif "private ad" in header.lower():
                    section = "PrivateAd"
                    ad_text = lines[1][6:].strip()
                    expiration_date = lines[2][17:].strip()
                    expiration_date_obj = datetime.datetime.strptime(expiration_date, "%d/%m/%Y")
                    days_left = (expiration_date_obj.date() - datetime.datetime.now().date()).days
                    formatted_entry = (
                        f"Private ad-------------\nText: {capitalize_sentence(ad_text)}\nExpiration date: {expiration_date}\nActual until: {expiration_date}, {days_left} days left\n\n"
                    )
                    sections["PrivateAd"].append(formatted_entry)
                elif "birth announcement" in header.lower():
                    section = "BirthAnnouncement"
                    child_name = lines[1][12:].strip()
                    birth_date = lines[2][12:].strip()
                    location = lines[3][10:].strip()
                    message = lines[4][9:].strip()
                    formatted_entry = (
                        f"Birth announcement-----\nChild name: {capitalize_sentence(child_name)}\nBirth date: {birth_date}\nLocation: {capitalize_sentence(location)}\nMessage: {capitalize_sentence(message)}\n\n"
                    )
                    sections["BirthAnnouncement"].append(formatted_entry)

        except Exception as e:
            print(f"Failed to process the file: {e}")
            raise

        return sections

    # Method to remove a file after processing
    def remove_file(self, file_path):
        try:
            os.remove(file_path)
            print(f"File {file_path} successfully removed.")
        except Exception as e:
            print(f"Failed to remove file {file_path}: {e}")


# Main execution point
if __name__ == "__main__":
    # Set the default folder via command-line argument if provided
    default_folder = sys.argv[1] if len(sys.argv) > 1 else "imports"
    ImportFromFile.default_folder = default_folder

    # Instantiate the NewsFeedGenerator and start it
    generator = NewsFeedGenerator()
    generator.start()