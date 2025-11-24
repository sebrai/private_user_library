# private_user_library

## 1. pages

**evil LM:**\
**Sebastian Branden:**\
**2IMI:**\
**10/11/25:**
**description:**\
*this is a hub for evil LM where you can see future plans, members and already executed missions*

### a. frontpage
*this is the frontpage of the site*

### b. members page
*this shows all mambers in evil_LM*

### c. accomplisments
*this show what evil_LM has completed*

### d. events page

*shows uppcomming events*
------------------------------------------------------------------------


## 2. Systembeskrivelse

**hub for memebers of evil LM**\
*the website shares what evil LM does and makes it easy for members to see future plans*

**uses:**\
*from any page you have acces to to go to a front page with info, memebers page containing all memebers, a accomplisments page where you see stuff that has already been completed and the companys future goals*

**Teknologier brukt:**

-   Python / Flask\
-   MariaDB\
-   HTML / CSS / JS\

------------------------------------------------------------------------

## 3. Server-, infrastruktur- og nettverksoppsett

### Servermiljø

*uses a flask python enviorment with flask, and mysql_connector installed*

### Nettverksoppsett

-   Nettverksdiagram
-   IP-adresser\
-   Porter\
-   Brannmurregler

Eksempel:

    Klient → Waitress → MariaDB

### Tjenestekonfigurasjon

-   systemctl / Supervisor\
-   Filrettigheter\
-   Miljøvariabler

------------------------------------------------------------------------

## 4. Prosjektstyring -- GitHub Projects (Kanban)

https://github.com/users/sebrai/projects/3/views/1

i use kanban to organize work

------------------------------------------------------------------------

## 5. Databasebeskrivelse

**Database name: evil_lm**

**Tables:**

**members:**
```
        +------------+--------------+------+-----+-----------+----------------+
        | Field      | Type         | Null | Key | Default   | Extra          |
        +------------+--------------+------+-----+-----------+----------------+
        | id         | int(11)      | NO   | PRI | NULL      | auto_increment |
        | name       | varchar(50)  | NO   |     | NULL      |                |
        | email      | varchar(100) | NO   | UNI | NULL      |                |
        | date_start | date         | YES  |     | curdate() |                |
        | role       | varchar(50)  | NO   |     | 'grunt'   |                |
        +------------+--------------+------+-----+-----------+----------------+
```
**done(old jobs):**
```
        +-------+--------------+------+-----+-----------------+----------------+
        | Field | Type         | Null | Key | Default         | Extra          |
        +-------+--------------+------+-----+-----------------+----------------+
        | id    | int(11)      | NO   | PRI | NULL            | auto_increment |
        | title | varchar(100) | NO   | UNI | NULL            |                |
        | descr | tinytext     | YES  |     | 'no decription' |                |
        | date  | date         | YES  |     | curdate()       |                |
        +-------+--------------+------+-----+-----------------+----------------+
```
**SQL-eksempel:**

**insert example**
``` sql
    INSERT INTO members(name,email) VALUES('yourname','your@email.com');
```

------------------------------------------------------------------------

## 6. Programstruktur

    evil_LM/
     ├── app.py
     ├── templates/
     ├── static/
     ├── .venv
     ├── .env
     └── password.txt
Databasestrøm:

    HTML(request) → Flask → MariaDB → Flask → HTML-tabell

------------------------------------------------------------------------

## 7. Kodeforklaring

Forklar ruter og funksjoner (kort).

------------------------------------------------------------------------

## 8. Sikkerhet og pålitelighet


-   Miljøvariabler\
-   Parameteriserte spørringer\
-   Validering\
-   Feilhåndtering

------------------------------------------------------------------------

## 9. Feilsøking og testing

-   Typiske feil\
-   Hvordan du løste dem\
-   Testmetoder

------------------------------------------------------------------------

## 10. Konklusjon og refleksjon

-   Hva lærte du?\
-   Hva fungerte bra?\
-   Hva ville du gjort annerledes?\
-   Hva var utfordrende?

------------------------------------------------------------------------

## 11. sources

-   w3schools\
-   flask.palletsprojects.com
