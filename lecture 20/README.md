## IMPORTANT
För att köra den här föreläsningsfilen, installera först PostgreSQL: pip install psycopg2-binary
Du behöver också installera programmet på din dator: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

När du kör koden kommer den inte att fungera från början. Du behöver:

- Starta pgadmin (används för att kolla på din databas)
- Öppna kommandotolken eller liknande verktyg
- Kör createdb -U <username> -h <hostname> -p <port> -e <database_name>, ersätt username, hostname, port och database_name
username är din användare, brukar vara postgres för standardservern
hostname brukar vara localhost
port brukar vara 5432
database_name sätter du själv

Du kan bli promptad att logga in, ange isf ditt lösenord

- Din databas är nu skapad!
- Skapa en config.py fil i samma directory som din skript fil du kör mot databasen, den kan se ut exempelvis såhär:

DB_HOST = ""
DB_PORT = 
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""

- Nu borde allt funka som det ska! Testa med test.py filen först

Finns flera sätt och kika att det funkar, via pgadmin är det:

- Klicka databasen du skapade, schemas, public, tables, ditt table och högerklicka query_tool, där skriv in:

SELECT * FROM your_table_name

kör koden så ska du se!


