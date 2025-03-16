# Import the datetime module for handling date and time
import datetime


# Define the base class `NewsFeedGenerator` which manages the news feed file
class NewsFeedGenerator:
    def __init__(self, file_name="news_feed.txt"):
        """
        Constructor for the base class.
        Sets the file name for the news feed file (default is 'news_feed.txt') and initializes it.
        """
        self.file_name = file_name  # Store the file name in an instance variable

    def read_existing_content(self):
        """
        Reads the existing contents of the file and categorizes it into sections:
        News, Private Ads, and Birth Announcements.
        Returns a dictionary containing these sections.
        """
        # Initialize sections as a dictionary with keys for section types
        sections = {"News": [], "PrivateAd": [], "BirthAnnouncement": []}
        current_section = None  # Track the current section being processed

        try:
            # Open the file in read mode and read all lines
            with open(self.file_name, "r") as file:
                content = file.readlines()  # Read file content line by line

            # Process each line in the file to group entries into sections
            for line in content:
                if line.startswith("News-------------------"):
                    # If the line starts with "News", switch to the News section
                    current_section = "News"
                    sections[current_section].append(line)
                elif line.startswith("Private Ad-------------"):
                    # If the line starts with "Private Ad", switch to the PrivateAd section
                    current_section = "PrivateAd"
                    sections[current_section].append(line)
                elif line.startswith("Birth Announcement-----"):
                    # If the line starts with "Birth Announcement", switch to the BirthAnnouncement section
                    current_section = "BirthAnnouncement"
                    sections[current_section].append(line)
                elif current_section:
                    # Append subsequent lines into the current section
                    sections[current_section].append(line)

        except FileNotFoundError:
            # Handle case where the file does not exist
            with open(self.file_name, "w") as file:
                # Create a new file with the header if it doesn't exist
                file.write("News feed:\n\n")
            print(f"File {self.file_name} created with default header!")
        except Exception as e:
            # Catch and print any other exceptions that occur during file reading
            print(f"An error occurred while reading the file: {e}")

        return sections  # Return the dictionary containing categorized sections

    def write_to_file(self, sections):
        """
        Write the updated sections back to the file.
        """
        try:
            # Open the file in write mode (this overwrites the file)
            with open(self.file_name, "w") as file:
                file.write("News feed:\n\n")  # Write the header to the file
                # Write each section in the desired order
                for section in ["News", "PrivateAd", "BirthAnnouncement"]:
                    for entry in sections[section]:
                        file.write(entry)  # Write each entry in the section
            print("Records updated in the file successfully!")  # Print success message
        except Exception as e:
            # Catch and print any error during writing
            print(f"An error occurred while writing to the file: {e}")

    def start(self):
        """
        Method to handle user menu options and interaction (main program loop).
        """
        sections = self.read_existing_content()  # Load existing content from the file

        while True:  # Infinite loop for user menu until "Exit" is selected
            # Display menu options to the user
            print("\nSelect what to add:")
            print("1. News")
            print("2. Private Ad")
            print("3. Birth Announcement")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")  # Take user input

            if choice == "1":
                # If user selects News, create a News instance to handle the entry
                news = News()
                entry = news.add_entry()  # Collect a new News entry
                sections["News"].append(entry)  # Add the entry to the News section
                self.write_to_file(sections)  # Write updated content back to the file
            elif choice == "2":
                # If user selects Private Ad, create a PrivateAd instance
                private_ad = PrivateAd()
                entry = private_ad.add_entry()  # Collect a new Private Ad entry
                sections["PrivateAd"].append(entry)  # Add the entry to the PrivateAd section
                self.write_to_file(sections)  # Write updated content back to the file
            elif choice == "3":
                # If user selects Birth Announcement, create a BirthAnnouncement instance
                birth_announcement = BirthAnnouncement()
                entry = birth_announcement.add_entry()  # Collect a new Birth Announcement entry
                sections["BirthAnnouncement"].append(entry)  # Add entry to the BirthAnnouncement section
                self.write_to_file(sections)  # Write updated content back to the file
            elif choice == "4":
                # Exit the program if user selects "Exit"
                print("Exiting. Goodbye!")
                break
            else:
                # Handle invalid input
                print("Invalid choice. Please select 1, 2, 3 or 4.")


# Define the `News` child class for handling news entries
class News:
    """
    Child class to handle specific behavior for adding news.
    """
    def add_entry(self):
        """
        Collects and formats data for a `News` entry.
        Ensures mandatory fields are not empty and returns the formatted entry.
        """
        while True:
            # Prompt the user for news text
            news_text = input("Enter the news text: ").strip()
            if news_text:  # Validate that the input is not empty
                break
            else:
                print("News text cannot be empty. Please enter a valid news text.")

        while True:
            # Prompt the user for the city
            city = input("Enter the city: ").strip()
            if city:  # Validate that the input is not empty
                break
            else:
                print("City cannot be empty. Please enter a valid city.")

        # Automatically generate the current date and time for publishing
        publish_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
        # Return the formatted News entry as a string
        return (
            "News-------------------\n"
            f"{news_text}\n"
            f"{city}, {publish_date}\n\n"
        )


# Define the `PrivateAd` child class for handling private ad entries
class PrivateAd:
    """
    Child class to handle specific behavior for adding private ads.
    """
    def add_entry(self):
        """
        Collects and formats data for a `Private Ad` entry.
        Ensures mandatory fields are not empty and returns the formatted entry.
        """
        while True:
            # Prompt the user for ad text
            ad_text = input("Enter the ad text: ").strip()
            if ad_text:  # Validate that the input is not empty
                break
            else:
                print("Ad text cannot be empty. Please enter a valid ad text.")

        while True:
            # Prompt the user for the expiration date
            expiration_date = input("Enter expiration date (DD/MM/YYYY): ").strip()
            try:
                # Parse the expiration date into a datetime object
                expiration_date_obj = datetime.datetime.strptime(expiration_date, '%d/%m/%Y')
                # Calculate the difference between the expiration date and today's date
                days_left = (expiration_date_obj.date() - datetime.datetime.now().date()).days

                if days_left < 0:
                    print("The expiration date has already passed. Please enter a future date.")
                elif days_left == 0:
                    print("The expiration date is today. The ad will expire at the end of the day.")
                    break
                else:
                    break  # Exit loop when the expiration date is valid
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        # Return the formatted Private Ad entry as a string
        return (
            "Private Ad-------------\n"
            f"{ad_text}\n"
            f"Actual until: {expiration_date}, {days_left} days left\n\n"
        )


# Define the `BirthAnnouncement` child class for handling birth announcement entries
class BirthAnnouncement:
    """
    Child class to handle specific behavior for adding birth announcements.
    """
    def add_entry(self):
        """
        Collects and formats data for a birth announcement entry.
        Ensures mandatory fields are not empty and returns the formatted entry.
        """
        while True:
            # Prompt the user for the child's name
            child_name = input("Enter the child's name: ").strip()
            if child_name:  # Validate that the input is not empty
                break
            else:
                print("Child's name cannot be empty. Please enter a valid name.")

        while True:
            # Prompt the user for the location
            location = input("Enter the location: ").strip()
            if location:  # Validate that the input is not empty
                break
            else:
                print("Location cannot be empty. Please enter a valid location.")

        while True:
            # Prompt the user for a short message
            message = input("Enter a short message about the child: ").strip()
            if message:  # Validate that the input is not empty
                break
            else:
                print("Message cannot be empty. Please enter a valid message.")

        while True:
            # Prompt the user for the birth date
            birth_date = input("Enter the birth date (DD/MM/YYYY): ").strip()
            try:
                # Parse the birth date into a datetime object
                birth_date_obj = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
                # Validate that the date is not in the future
                if birth_date_obj > datetime.datetime.now():
                    print("Birth date cannot be in the future. Please enter a past date.")
                else:
                    break
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        # Return the formatted Birth Announcement entry as a string
        return (
            "Birth Announcement-----\n"
            f"Welcome {child_name}!\n"
            f"Born on {birth_date}\n"
            f"Location: {location}\n"
            f"Message: {message}\n\n"
        )


# Main script execution
if __name__ == "__main__":
    # Create an instance of the NewsFeedGenerator base class
    generator = NewsFeedGenerator()
    # Start the user interaction loop
    generator.start()