# Simply Jet 

As an exercice, you'll be asked to create a simple Django web app.

## Models

### `User`

A `User`, authenticating via their email address and a password. 

Users can be added and managed via the Django admin interface, no need to add extra views to manage them.


### `UploadedFile` and `UploadGroup`


An `UploadGroup` stores:

- The `User` that created the group
- Date and time of creation


An `UploadedFile` should store the following information:

- A reference to the `UploadGroup` which it belongs to
- A file
- A user editable title
- An MD5 Hash of the file

## Views

The following views are required:

### Homepage / main view.

If the current user isn't authenticated, redirect them to the login view

The main view consist of a form where the (authenticated) user can upload up to 10 files.

In its initial state, the form has one "row" containing:
- An input field (type=text) for the name
- An file input field

By clicking a button, the user can add additional empty rows, having the same fields as the original row.

The user can remove individual rows using a "remove" button next to each row.

When the user submits the form, the server should:

1. Create a new `UploadGroup`
2. Create a new `UploadedFile` for each submitted row and link it to the group.:

  - The file and user editable title are taken from the given row
  - The MD5 Hash should be computed by POSTing the *binary contents* of the file to the [Hashify API](https://documenter.getpostman.com/view/3362843/RWMCt9WU).

3. Redirect to a "results view" (the URL contains the id of the generated Group)


### Results view

On the results view, we display a table with all the `UploadedFile` (one per row) displaying:

- The user title of the file
- It's MD5 hash
- A link to download the file.

There should also be a way of downloading the content of the table as an Excel document containing the same information.

### Login view

Login form to authenticate the user via their username and password.




## Notes

- All the views (except for the Login view) should be authenticaed.
- Style / design: feel free to use any design / CSS framework you wish, or none at all
- Tests: feel free to write unit tests if you think it might help

## Submission

- Submit your project as a new pull request.
- The submitted code should be complete and it should be "ready to run" (`python manage.py migrate`, `python manage.py createsuperuser`, `python manage.py runserver`)
