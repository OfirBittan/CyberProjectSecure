import psycopg2
import psycopg2.extensions
import re


# Escape a string, making it safe to use in a SQL query.
# This is how the string will loose it's special meaning regarding sql.
def escape_string(search_term):
    secure = psycopg2.extensions.QuotedString(search_term).getquoted().decode('utf-8')
    return secure.strip("'")


# Escape a string, making it safe to use regarding Secured XSS.
def sanitize_and_escape(input_string):
    # Remove any HTML tags and their content
    sanitized_string = re.sub(r'<.*?>', '', input_string)
    # Remove any non-alphanumeric characters using regular expression
    sanitized_string = re.sub(r'[^a-zA-Z0-9\s]', '', sanitized_string)
    sanitized_string = ' '.join(sanitized_string.split())
    return sanitized_string
