# [[GEE-BLOG]]

## AUTHOR'S NAME

- Odoyo Grace Awino

## DESCRIPTION

- This  is a flask application that allows writers to post blogs, edit and delete blogs. It also allows users who have signed up to comment on the blogs that has been posted by a writer. It also allows a person be subscribed to recieve email everytime a new blog is posted by a writer.

## USER STORY

* A user can view the most recent posts.
* View and comment the blog posts on the site.
* A user should an email alert when a new post is made by joining a subscription.
* Register to be allowed to log in to the application
* A user sees random quotes on the site
* A writer can create a blog from the application and update or delete blogs I have created.

## BDD

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all blogs, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with blogs that have been posted by writes and be able to subscribe to the blog|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments tamplate with your comment and other comments|
|Subscription | **Email Address**| Flash message "Succesfully subsbribed to Gee-blog"|

## TECHNOLOGIES USED

* Python3.6
* Flask
* Javascript
* Heroku






