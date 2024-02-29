import psycopg2
import psycopg2.extensions


# Escape a string, making it safe to use in a SQL query.
# This is how the string will loose it's special meaning regarding sql.
def escape_string(search_term):
    secure = psycopg2.extensions.QuotedString(search_term).getquoted().decode('utf-8')
    return secure.strip("'")
