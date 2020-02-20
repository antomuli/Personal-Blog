# Title

**Personal_Blog**

## Description
Anto's blog is a personal blogging website where you can create and share your opinions and other users can read and comment on them. It  also has random quotes that inspire the users.  You can visit the live site on **link**

## Author


* [**Anthony Muli**](https://github.com/antomuli)

## Features


As a user of the web application you will be able to:

1. See all blogs
2. Create an account
3. Log in
4. Create a blog
5. Comment on a blog
6. See comments posted on each individual blog
7. Edit your profile i.e will be able to add a short bio about yourself and a profile picture



## CODEBEAT

[![codebeat badge](https://codebeat.co/badges/6feab53a-468f-4b8c-b6bf-1ac5d10bfcd1)](https://codebeat.co/projects/github-com-antomuli-1_minute_pitch-master)

## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/antomuli/Personal-Blog.git
        $ cd 1_Minute_Pitch

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` by commenting on `production` instance and uncommenting `development` instance
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py server
        
## Technologies Used
* Python3.6
* Flask
* HTML
* Bootstrap

This application is developed using [Python3.6](https://www.python.org/doc/), [Flask](http://flask.palletsprojects.com/en/1.1.x/), [HTML](https://getbootstrap.com/) and [Bootstrap](https://getbootstrap.com/)

## Known Bugs
* The blog doesn't meet all the user's stories/needs.

* The user may have some difficulty in profile handling and management since it's still under development.

## Support and Team
Anthony Muli and fellow colleagues

### License

MIT License

Copyright (c) 2020 Moringa School-***Anthony Muli***

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.