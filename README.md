# Perexma
:construction: This documentation is _work in progress_.

## Description
_Perexma_ project is a **Per**sonal **Ex**penses **Ma**nager built with Django.

## Features
1. See expenses
1. Save expenses
1. ...

## Business requirements
### Brainstorm
1. Register _income_ & _expenses_
1. Page to see pending bills or payments
1. Display expenses for a specific date range
    - It might have default options such as: _monthly_, _weekly_, _daily_
    - Custom range specified by the user
1. Ability to register _loans_ and _borrowings_
1. Insight of what is left to be spent (like)
1. Provide a module with charts for overall analysis
1. Page for capital or resources
1. Savings
1. Won/loss of products such as Cta Ahorro, Fiducuenta, Plan Semilla
1. Credit card shopping
    - Type "close date"
    - Type "due date"
    - Save automatically the payments done with that product
1. Page for "comprobante" with home bills
1. Save images with bills
1. Insight: "pending to be paid for current month (cycle).
1. Page for crypto coins
1. Cycle forecast
1. Summary: Page for green table: IN|OUT|DIFF
1. Analyse implementation with Bancolombia API
1. ...


### Open questions
1. :question: Where to record Pereira expenses? This is a pretty custom expense. How can make it some sort of generic? Especially for what I need to know the expenses list per month as not all months have exactly the same expenses.
1. Voice recording to get text. Is it possible to translate that into API requests? In the same fashion as Selenium bots

### Modules
List of modules. The ones with :heavy_check_mark: mark are already in Figma.
1. ✓ Admin (django default)
    + Users
    + Transaction (movement type):
        - Income: Base Salary, AFC, Crypto, etc.
        - Expense type: Food, Health, Education, Home Bills, etc. 
    + Resource: Cash, Savings account, Credit Card, Crypto, Wallet, etc. (purple table)
    + Currency: COP, USD, EUR, ARS...
    - Saving: Lolo, Predial, Declaración, Babe, etc.
    + Settings:
        - cycle
1. ✓ Home
    + ✓ Insights: 
        - ✓ What is left to be spent ("Wiiii")
    + ✓ Summary: Upcoming bills
1. :wrench: Register
    + ✓ Income & Expenses
    + :question: Loans & Borrowings
    + ✓ Savings
1. :question: Analytics
    + Display expenses: monthly | weekly | daily | custom
    + Pie chart per type (as spreadsheet)
1. Bills
    + ✓ Pending bills (blue table)
    + :question: Paying bills: add payment and send email
1. Page for green table: IN|OUT|DIFF
    + :question: create db view to get this info
1. Investment
    + Won/loss of products such as Cta Ahorro, Fiducuenta, Plan Semilla
    + Crypto
1. Credit card shopping
    - Type "close date"
    - Type "due date"
    - Save automatically the payments done with that product
1. Cycle forecast
...

### Mockups
:art: [WIP] Figma prototype, [here](https://www.figma.com/proto/jpNcJYN0gp24hvZocYYDtg/Perexma?node-id=3-4&scaling=scale-down&page-id=0%3A1)


### Entity-Relation diagram
:art: [WIP], [here](https://lucid.app/lucidchart/360d6741-911d-4a84-b0be-ecbaf6025a53/edit?viewport_loc=569%2C340%2C1696%2C840%2C0_0&invitationId=inv_092a0e6b-3605-4f66-b7a1-b117aba9af66)


# Database

## Start postgres instance

This command will build an image called "postgres" based on `Dockerfile` file.
```
docker build -t postgres .
```

There's another way in case we need to load password using env var `POSTGRES_PASSWORD` from `.env` file through `--build-arg` argument.
```
sudo docker build --build-arg POSTGRES_PASSWORD=$(cat .env | grep POSTGRES_PASSWORD | cut -d'=' -f2) -t postgres_img .
```

## Run docker container

This command will run a container called `postgres_perexma` in background / _daemon_ mode (-d). 
```
docker run -d --name postgres_perexma --env-file .env -p 5432:5432 postgres
```
From command above
- `--name postgres_perexma` indicates the new container name
- `postgres` at the end, refers to the docker image.


# Developer
## Env vars
Create `.env` file with the following variables:
```
SECRET_KEY=<value>
POSTGRES_HOST=<value>
POSTGRES_PORT=<value>
POSTGRES_DB_NAME=<value>
POSTGRES_USER=<value>
POSTGRES_PASSWORD=<value>
```
## Summary list:
- Django proyect: perexmadj
- Django app: 

# Useful links
1. [Gitmoji.dev](https://gitmoji.dev/), an emoji guide for your commit messages :sunglasses:
2. [Complete list](https://gist.github.com/rxaviers/7360908) of github markdown emoji markup :v:
