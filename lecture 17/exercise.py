import threading
import urllib.request
import os

"""
Exercise!:
Create a program that downloads an image from several urls using a thread for each download!

Tip: os lib is meant for things such as folders, urllib.request.urlopen is common for requests
"""


# Function to download an image from a URL
def download_image(url, destination):
    # Downloads an image from a URL
    pass


# Function to download a list of images concurrently
def download_images(urls, destination_folder):
    # Create a thread for each url that for each thread calls on the download_image func!

    # en tråd per url, tråden körs på download_image() och skicka med parameterar
    pass


if __name__ == "__main__":
    image_urls = [
        "url_of_image_1",
        "url_of_image_2",
        "url_of_image_3",
        # Add more image URLs as needed
    ]

    # Switch to the path to your folder
    destination_folder = "path_to_destination_folder"

    # Call the download_images function with the image URLs and destination folder
    download_images(image_urls, destination_folder)
