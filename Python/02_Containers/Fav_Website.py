import webbrowser


def open_website(url):
  """
  Opens the given website in Firefox.

  Args:
    url: The URL of the website to open.
  """

  webbrowser.open("https://github.com/AbdelrhmanSalahAboelenin/Embedded-Linux-2023", "firefox")

import favorite_websites



  # Get a list of the favorite websites.
websites = favorite_websites.get_websites()

  # Print a menu of the websites.
print("Choose a website to open:")
for index, website in enumerate(websites):
   print(f"{index + 1}: {website}")

  # Get the user's choice.
choice = int(input("Enter your choice: "))

  # Open the selected website.
favorite_websites.open_website(websites[choice - 1])



