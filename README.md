# Django-Server-Apps

Django based applications for better tracking of activities and processes

View the app live at https://chase-sawyer-demos.herokuapp.com/

- KeysApp: For tracking loans of keys, including overdue status and loss.
- rttApp: Repair Task Tracker - For processing Desktop Computer and other hardware repairs and maintenance.

## Tech Stack - Major Components

- Python3
- Django
- PostgreSQL
- GraphQL \(Graphene + Apollo\)
- Vue.js

## Development Info - Django Core

The Django core has the admin interface for managing/provisioning users, user authentication links, and administrative tasks related to editing linked database models that aren't exposed to the user interface(s).

## Development Info - KeysApp

The basic features for checkout, return, and renewal are in place. Django administration pages allow for insertion/deletion of keys, departments, etc. from the database.
Demo site / proof of concept complete.
This site would act as a front end to allow the self-service management of \(brass\) keys checked out to various groups in an organization

### Security - KeysApp

Inherent risk in users not supplying the correct information, as it is not validated or verified by any authority. A basic enhancement would involve a user authentication / sign-up process that validated the supplied email address belongs to the user before they are allowed to check out any keys, or one in which another trusted authority could be validated against using user credentials \(eg. SSO, federated login, etc.\).

### Major Needs - KeysApp

- [ ] Production environment settings
- [x] Server space
  - Cloud hosting possible through Heroku, Google Cloud Platform, AWS, etc.
- [x] Production database backend \(postgresql\)
- [ ] Logging utility setup and sink
- [ ] Automated jobs to update certain database features: (check Celery)
  - Overdue flag
  - Key Retirement

### Core Functionality - KeysApp

- Customer Actions (forms)
- [x] Checkout
- [x] Return
- [x] Renew
- [ ] Create a new department \(currently possible through the admin interface only\)
- Model
  - Tables
    - Affiliations
    - Customers
    - Departments
    - Key Types
    - Keys
    - Loan Exceptions
    - Loan Terms
    - Records
  - Features
    - Overall all rows in the database tables have automatic time stamping for insertion and updates.
    - Records
      - Are the definitive record of an association of a Customer and a Key
      - Can be 'Returned', 'Checked out', 'Overdue', 'Lost/Broken', and 'Paid' \(status\)
      - Is considered active unless it is 'Returned' or 'Paid'
    - Keys
      - are either active \(default\) or retired
      - cannot be checked out if retired
    - Customers
      - Uniquely identified by email address
      - No account creation needed - system tries to match up as many key records as possible to individuals by using their email addresses as unique identifiers
      - addresses a unique use case in which verifying email addresses is not possible
    - Departments
      - Can have a authoritative administrative contact entered as a backup contact for Customer
  - Integrity
    - Keys that are checked out can only be returned or renewed
    - Keys that are returned can only be checked out
    - Affiliation controls whether customer NetID is required to be entered
    - Customers are updated or inserted based on email unique-ness
    - System checks email against associated checkout records
      - Customer cannot check out more than 1 of any type of key without an exception
      - Exceptions have a limit and an expiration
      - Exceptions must be granted by a Staff member \(via Admin interface\)

#### Derivative Policy Implications - KeysApp

- There is no such thing as a 'forever' loan

While it's technically possible to set the due date to some date in the distant future, such as 2050, there is no provision for a loan to remain valid forever. Best practice going forward should involve a annual \(or other regular interval\) review of access privileges that staff have, with keys that are needed being extended, and keys that are no longer needed due to changes in staff roles or positions being returned.

### Future Features - KeysApp

- [ ] Off-Campus / outside customers will still need a "department" - should decide what gets entered for this field \(organizational management?\)
- [ ] Automatic loan due date entry based on Loan Term
  - Needs a calendar in the database defining term end dates for form to default due dates to automatically
- [ ] Ability to check out multiple keys \(of various types\) to a single customer within a single session/transaction
- [ ] Admin: customization - branding, styles, etc.
- [ ] Account controls for staff to administer system
- [ ] Record histories \(more detail\) for edits to the database made by all forms
- [ ] Error pages
- [ ] Testing code to ensure data validation through future releases
  - Existing test code incomplete - does not cover every function/use case.

#### Additional features as requested / time allows - KeysApp

### External Resources - KeysApp

The following libraries, etc are used in support of this project:

- Django 1.11
- Bootstrap 3.2
- FontAwesome 4.5
- jQuery 3.2.1
- jQuery UI 1.12.1

## Development Info - RttApp

The basic look and feel have been fleshed out, but functionality is still pending completion.

### Major Needs - RttApp

- [x] Server Instance
- [x] Authentication enforced for user access
  - Uses Google as authentication authority
- [x] Admin interface

### Core Functionality - RttApp (UI)

- [ ] Create new report
  - [ ] Pick hardware from a list
    - [ ] If not present, create a new piece of hardware
  - [ ] Choose from a list of common issue categories
- [x] Search for issues by asset number
- [x] View report
- [ ] Update report
  - [ ] Make notes about repair and state of issue/report
  - [ ] Change status of report (New/In Progress/Stalled/Resolved)
  
### Core Functionality - RttApp (Model)

- Data Validation Rules
  - [x] Reports that are 'Resolved' can no longer be modified in any way without their state being reverted to another state.
    - Validated at the model level, should still implement a front-end matching validation rule, or integrate into GraphQL data

### External Resources - RttApp

RTT is a Vue.js single page app, which communicates to the Django back end with GraphQL.
Major tech components:

- Vue
- Yarn/node
- GraphQL \(Apollo\)
- Tachyons \(style\)
