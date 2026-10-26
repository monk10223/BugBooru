# BugBooru

A booru-style image board for bugs. Users post images by URL, tag them, search by tags, and comment. Built with Django for the SoftUni Django Basics exam.

## Features

- Post images with comma-separated tags (letters and underscores only)
- Search by tags (all tags must match), paginated results
- Edit a post's tags, delete posts with confirmation
- Comments on posts (edit and delete included) and a recent comments page
- Top tags ranking and a tag sidebar with counts

## Apps

| App | Responsibility |
|---|---|
| `posts` | Posts, search, tag editing |
| `comments` | Comments on posts, recent comments |
| `tags` | Tags and the top tags ranking |

## Models

- `Post` (image URL, author, created date) with a many-to-many relation to `Tag`
- `Comment` (text, author, created date) with a many-to-one relation to `Post`
- `Tag` (unique name)

## Setup

1. Clone the repository and enter the folder.
2. Create and activate a virtual environment: `python -m venv .venv`
3. Install Django: `pip install django`
4. Apply the migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
6. Open http://127.0.0.1:8000/

The database is SQLite and needs no setup or environment variables. The database starts empty; create posts, tags and comments from the site's navigation.

## Pages

| URL | Page |
|---|---|
| `/home/` | Home with search |
| `/posts/` | Post list and search |
| `/posts/create/` | New post |
| `/posts/<id>/` | Post details and comments |
| `/comments/` | Recent comments |
| `/tags/` | Top tags |