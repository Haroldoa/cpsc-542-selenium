import psycopg2.extras
con_string = "host='localhost' dbname='odoo15Ning1' user='odoo' password='odoo'"
con = psycopg2.connect(con_string)
cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
print('show the first row of the table account_account')
cursor.execute ('SELECT * from account_account')
row = cursor.fetchone()
print(row)
print('show the first row of the table estate_property')
cursor.execute ('SELECT * from estate_property')
row = cursor.fetchone()
print(row)