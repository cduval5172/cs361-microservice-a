# Microservice A
## Description
This program receives a keyword from a main program and then searches and downloads 5 images related to the keyword. The images are saved in a directory called downloaded_images.
## How to request data
Make a post request to the url 'http://localhost:5001/search_image'. Include a keyword in the post request.

Here is some example code:

url = 'http://localhost:5001/search_image'

data = {'keyword': 'basketball'}

response = requests.post(url, json=data)
## How to receive data
The downloaded images will populate a folder called downloaded_images. You can access the images with the path 'project_root/downloaded_images'.
## UML Sequence Diagram
<img width="521" alt="Screen Shot 2024-08-07 at 4 53 22 PM" src="https://github.com/user-attachments/assets/c8270a65-3b35-48a0-9394-06495103a8e4">
