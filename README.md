# Gallery App
#### This is a Python web application using Django  framework and Postgresql, 2019
#### By **[mainamurage](https://github.com/mainamurage)**
## Description
This is My personal web application which acts as Gallery store, Where i can upload images based on location or either category,Other users can see and view my images they can search and select by location. Users can view a single image with all the details about the image, Simple terms an online Gallery
## Setup/Installation Requirements
* A PC mainly with an Operating system.
* Python3.6 or later is installed in your PC.
* Postgresql installed
* clone the directory into your local machine
* navigate to the cloned folder by `cd Gallery_Studio`
* Create a virtual environment
* run `source virtual/bin/activate`
* install Django `pip install django=1.11`
* pip install `requirements.txt`
* run `python3.6 manage.py runserver `
* The application should work
* for the test run `python manage.py test image_studio`
## Known Bugs
NO known bugs as at the moment please reach to us if you see any.
## Behavior Driven Development

| __Behavior__  | __Input example__ | __Output example__ |
| ------------- | ----------------- | ------------------ |
| The user should be able to view all The Photos on the home page  | "https://www.com"   | photos  |
| The application should give the user an option to view photos based on location| Karen | images taken in karen |
| The application should be able to save uploaded images | image | status saved|ok |
| The user should be able to search any photo based on category | search | searched photo |
| The application should restrict only the user with privileges to access admin panel | user/admin | unauthorized/access |
| The application should be able to update images | update | true |
| The user should be able to click a button and get the link of the image saved to the clipboard | click | saved |
| The application should provide a large view for image display | view | view |


## Technologies Used
## main languages used are
* Python
* Material design
* WhiteNoise
* Amazon s3
* JavaScript
* CSS
* Django
* PostgreSQL Database

## Support and contact details
get me at adrianmaina21@gmail.com
### License
[MIT LICENCE](LICENSE)
Copyright (c) 2019 **maina murage**
This software is free to use and distribute, Therefore all rights and given to any user to modify and either use for Commercial purpose or local purpose.