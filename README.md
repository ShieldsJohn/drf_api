# Cat Snaps API

This is the back-end API used by the React application, [Cat Snaps](https://github.com/ShieldsJohn/cat-snaps)


## Project Aim

The aim of this API is provide database CRUD and user authentication functionality to Cat Snaps (insert deployed link) - a photo-sharing social media site, including features such as user profiles, posting images, commenting on and reacting to posts and following other users.



## Project Structure

The structure of this API project is based on Code Institute's Django Rest Framework API walkthrough project.  I have created additional models and customised some existing models to tailor the API to the needs of the Cat Snaps application.


## User Stories

### Profiles

- As a developer, I want to create a profile when a user is created.
- As a developer, I want to be able to view a list of profiles.
- As a user I can view a profile.
- As a user, I would like to be able to edit my profile information.

### Posts

- As a user I want to be able to create and list posts.
- As a user, I want to able to view, update or delete a post.

### Comments

- As a logged in user I would like to be able to create, list and delete comments on posts.

### Reactions

- As a developer, I want users to be able to react to other users' posts and for me to see a list of these reactions.
- As a developer, I want users to be able to deselect their reaction and delete any record of it having happened.

### Saved Posts

- As a developer, I want users to be able to save their favourite posts by other users and for superusers to see a list of these saved posts.
- As a user, I want to able to be able to retrieve and delete saved posts.

### Followers

- As a developer I would like users to be able to follow each other and for me to see a list of who is following.
- As a user, I want to be able to unfollow a user I have previously followed.

### Contact

- As a developer, I would like my users to be able to complete a contact form and for superusers to see a list of these contacts.
- As a user, I want to able to view and delete a submitted contact form.

