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


## Agile

This API was planned using Agile methodology and MoSCoW prioritisation on GitHub Projects.

I created Epics for each feature and broke this down into Sprints, driven by User Stories.   Each User story/feature was prioritised as either Must have, Should have, Could have or Won't have.  Each task was moved through the kanban as the tasks progressed from To Do, In Progress, to Done.

The Epics can be found [here](https://github.com/ShieldsJohn/drf_api/milestones) and the kanban found [here](https://github.com/users/ShieldsJohn/projects/6).


## Database

### Models

I struggled to find a free tool which would allow me to accurately depict my database, so I have provided relationships commentary for clarity.

These are the models in the database of this API:

- User.  Per DRF User model.  Has a one to one relationship with Profile, a one to many relationship with Comment, a many to many with Following, a one to many with Reaction and a one to many with Saved Post.
- Profile.  Customised to include bio and social media links. Has a one to one relationship with User and a one to many with Post.
- Post. Customised to include captions. Has a many to one relation to Profile, a one to many relationship with Reaction, a one to many relationship with Comment and a one to one relationship with Saved Post.
- Comment. Per DRF API walkthrough. Has a many to one relationship with User and a many to one relationship with Post.
- Reaction.  Customised to include reaction type. Has a many to one relation ship with User and a many to one relationship with Post.
- Following.  Per DRF API walkthrough. Has a many to many relationship with User.
- Saved Post.  Custom model to facilitate saving favourite posts.  Has a many to one relationship with User and a one to one relationship with Post.
- Contact.  Custom model to facilitate a contact form for users to contact Cat Snaps. Has no database relationships.

![entity relationship diagram](/workspace/drf_api/readme_images/erd.png)
/workspace/drf_api/readme_images/erd.png


### Create, Read, Update and Delete (CRUD)

This API and its database is designed with CRUD functionality in mind.  The following methods are used to carry out CRUD:

- POST (send data to database to create or update)
- GET (retrieve data from the database)
- PUT (update exisiting data, or create new data in database)
- DELETE (delete data from the database)

As a result, users of the API can apply the following functionality:

- Profiles (CRU)
- Posts (CRUD)
- Comments (CRUD)
- Reactions (CRUD)
- Followers (CRUD)
- Contact (C)

