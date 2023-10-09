import re

def build_sql_update_email_by_id(email, user_id):
    if not (re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) and re.match(r'^\d+$', str(user_id))):
        raise ValueError("Neplatný vstup")
    return f"UPDATE uzivatel SET email = '{email}' WHERE id = {user_id}"

def build_sql_delete_all_by_table(table_name):
    if not re.match(r'^[a-zA-Z0-9_]+$', table_name):
        raise ValueError("Neplatný název tabulky")
    return f"DELETE FROM {table_name}"

def build_sql_update_users(users):
    sql = ""
    for i, user in enumerate(users):
        if not (re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', user["email"]) and re.match(r'^[a-zA-Z0-9_]+$', user["jmeno"])):
            raise ValueError(f"Neplatný vstup pro uživatele na pozici {i}")
        sql += f"UPDATE uzivatel SET email = '{user['email']}', jmeno = '{user['jmeno']}' WHERE id = {i};\n"
    return sql
