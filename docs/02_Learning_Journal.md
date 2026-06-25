# Day 1 - Django Foundation

## What I Learned

- Difference between Django Project and App
- How models work
- What migrations are
- How Django Admin works
- How data is stored in a database

## What I Built

- HeartSync Django Project
- Patients App
- Patient Model
- Admin Dashboard Access

## Challenges Faced

- Python installation issue
- Broken pip configuration
- Accidentally stopped Django server using Ctrl+C

## Outcome

Successfully created and managed patient records through Django Admin.


# Day 2

## Topics Learned

- Django URLs
- Django Views
- Django Templates
- HTTP GET Requests
- HTTP POST Requests
- Form Handling
- Database Insert Operations
- Querying Data with ORM

## What I Built

Created a Patient Registration Form that:

- Accepts patient details
- Saves data into SQLite database
- Displays all registered patients dynamically

## Key Learning

The request flow in Django:

Browser → URL → View → Model → Database → Template → Browser

## Challenges Faced

- Encountered "view didn't return HttpResponse" error
- Learned that every Django view must return a response
- Fixed indentation issue in Python