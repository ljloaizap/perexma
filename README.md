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
1. ...

### Modules
1. Admin (django default)
    - Product type
        - Savings Account
        - Fiducuenta
        - Plan Semilla
        - Crypto
1. ...


# Useful links
1. [Gitmoji.dev](https://gitmoji.dev/), an emoji guide for your commit messages :sunglasses:
2. [Complete list](https://gist.github.com/rxaviers/7360908) of github markdown emoji markup :v:
