import datetime


class NewsFeedGenerator:
    def __init__(self, file_name="news_feed.txt"):
        """
        Parent class to handle common functionality for the news feed file.
        """
        self.file_name = file_name
        # Ensure the file starts with the header
        self.initialize_file()

    def initialize_file(self):
        """
        Ensures the file has the default header 'News feed:' at the beginning.
        This runs when the object of the class is initialized.
        """
        try:
            # Check if the file exists and is not empty
            if not self.check_file_exists_and_has_content():
                with open(self.file_name, "w") as file:
                    # Write the default header
                    file.write("News feed:\n\n")
                print(f"Default header 'News feed:' added to {self.file_name}!")
        except Exception as e:
            print(f"An error occurred while initializing the file: {e}")

    def check_file_exists_and_has_content(self):
        """
        Checks if the file exists and contains data.
        Returns True if the file exists and is not empty, False otherwise.
        """
        try:
            with open(self.file_name, "r") as file:
                content = file.read()
                # Check if the file contains content
                return bool(content.strip())
                # File doesn't exist
        except FileNotFoundError:
            return False

    def write_to_file(self, entry):
        """
        Method to write content to a file.
        """
        try:
            # Open the file in append mode
            with open(self.file_name, "a") as file:
                # Write the provided entry to the file
                file.write(entry)
            print("Record published successfully!")
        except Exception as e:
            # Handle errors (e.g., permission issues, disk space)
            print(f"An error occurred while writing to the file: {e}")

    def start(self):
        """
        Method to handle user menu options and interaction.
        """
        while True:
            print("\nSelect what to add:")
            print("1. News")
            print("2. Private Ad")
            print("3. Birth Announcement")
            print("4. Exit")
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                # Create an instance of the News child class
                news = News(self.file_name)
                # Call the add_entry method of News
                news.add_entry()
            elif choice == "2":
                # Create an instance of PrivateAd
                private_ad = PrivateAd(self.file_name)
                # Call the add_entry method of PrivateAd
                private_ad.add_entry()
            elif choice == "3":
                # Create an instance of BirthAnnouncement
                birth_announcement = BirthAnnouncement(self.file_name)
                # Call the add_entry method of BirthAnnouncement
                birth_announcement.add_entry()
            elif choice == "4":
                # Exit the loop and end the program
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3 or 4.")


class News(NewsFeedGenerator):
    """
    Child class to handle specific behavior for adding news.
    """
    def add_entry(self):
        """
        Collects and formats data for a `News` entry, then writes it to the file.
        Ensures mandatory fields are not empty.
        """
        # Prompt user for the news text (Mandatory field)
        while True:
            # Remove extra whitespace
            news_text = input("Enter the news text: ").strip()
            # Check if not empty
            if news_text:
                break
            else:
                print("News text cannot be empty. Please enter a valid news text.")

        # Prompt user for the city (Mandatory field)
        while True:
            # Remove extra whitespace
            city = input("Enter the city: ").strip()
            # Check if not empty
            if city:
                break
            else:
                print("City cannot be empty. Please enter a valid city.")

        # Automatically generate the current date-time
        publish_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')

        # Format the entry string
        entry = (
            "News-------------------\n"
            f"{news_text}\n"
            f"{city}, {publish_date}\n\n"
        )

        # Save to file using the parent class method
        self.write_to_file(entry)


class PrivateAd(NewsFeedGenerator):
    """
    Child class to handle specific behavior for adding private ads.
    """

    def add_entry(self):
        """
        Collects and formats data for a `Private Ad` entry, then writes it to the file.
        Ensures that `ad_text` and `expiration_date` fields are mandatory.
        """
        # Prompt user for the ad text (Mandatory field)
        while True:
            ad_text = input("Enter the ad text: ").strip()
            if ad_text:
                break
            else:
                print("Ad text cannot be empty. Please enter a valid ad text.")

        # Prompt user for the expiration date (Mandatory field)
        while True:
            expiration_date = input("Enter expiration date (DD/MM/YYYY): ").strip()
            try:
                expiration_date_obj = datetime.datetime.strptime(expiration_date, '%d/%m/%Y')
                days_left = (expiration_date_obj.date() - datetime.datetime.now().date()).days

                # Expiration date is in the past
                if days_left < 0:
                    print("The expiration date has already passed. Please enter a future date.")
                # Expiration date is today
                elif days_left == 0:
                    print("The expiration date is today. The ad will expire at the end of the day.")
                    break
                else:
                    break  # Exit loop if expiration date is valid
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

        # Format the entry string
        entry = (
            "Private Ad-------------\n"
            f"{ad_text}\n"
            f"Actual until: {expiration_date}, {days_left} days left\n\n"
        )

        # Save to file using the parent method
        self.write_to_file(entry)


class BirthAnnouncement(NewsFeedGenerator):
    """
    Child class to handle specific behavior for adding birth announcements.
    """

    def add_entry(self):
        """
        Collects and formats data for a birth announcement entry, then writes it to the file.
        Ensures that all fields are mandatory, with immediate feedback for missing or invalid inputs.
        """

        # Prompt user for the child's name (Mandatory field)
        while True:
            # Remove extra whitespace
            child_name = input("Enter the child's name: ").strip()
            # Check if not empty
            if child_name:
                break
            else:
                print("Child's name cannot be empty. Please enter a valid name.")

        # Prompt user for the location (Mandatory field)
        while True:
            # Remove extra whitespace
            location = input("Enter the location (e.g., hospital or city): ").strip()
            # Check if not empty
            if location:
                break
            else:
                print("Location cannot be empty. Please enter a valid location.")

        # Prompt user for a message (Optional but ensure it's not empty)
        while True:
            # Remove extra whitespace
            message = input("Enter a short message about the child: ").strip()
            # Ensure it's not empty
            if message:
                break
            else:
                print("Message cannot be empty. Please enter a valid message.")

        # Prompt user for the birth date (Mandatory field)
        while True:
            birth_date = input("Enter the birth date (DD/MM/YYYY): ").strip()  # Ask for the birth date
            try:
                # Parse the birth date and ensure the format is correct
                birth_date_obj = datetime.datetime.strptime(birth_date, '%d/%m/%Y')

                # Validate the birth date (must be a past date)
                if birth_date_obj > datetime.datetime.now():
                    print("Birth date cannot be in the future. Please enter a valid past date.")
                elif birth_date_obj.year < 1900:
                    print("Invalid year! Please enter a realistic year (e.g., after 1900).")
                else:
                    break  # Exit the loop if the date is valid
            except ValueError:
                # Handle invalid date inputs
                print("Invalid date format. Please use DD/MM/YYYY.")

        # Format the birth announcement entry
        entry = (
            "Birth Announcement-----\n"
            f"Welcome to the world, {child_name}!\n"
            f"Born on: {birth_date}\n"
            f"Location: {location}\n"
            f"Message: {message}\n\n"
        )

        # Save to file using the parent method
        self.write_to_file(entry)

if __name__ == "__main__":
    generator = NewsFeedGenerator()  # Create an instance of the parent class
    generator.start()  # Start the user interaction