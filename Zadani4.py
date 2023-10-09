import re

def build_sql_update_user_jmeno_by_id(name, user_id):
    if not (re.match(r'^[a-zA-Z0-9_]+$', name) and re.match(r'^\d+$', str(user_id))):
        raise ValueError("Neplatný vstup")
    return f"UPDATE uzivatel SET jmeno = '{name}' WHERE id = {user_id}"

def build_sql_delete_by_table_and_id(table_name, record_id):
    if not (re.match(r'^[a-zA-Z0-9_]+$', table_name) and re.match(r'^\d+$', str(record_id))):
        raise ValueError("Neplatný vstup")
    return f"DELETE FROM {table_name} WHERE id = {record_id}"

def build_sql_insert_users(users):
    sql = ""
    for user in users:
        if not (re.match(r'^[a-zA-Z0-9_]+$', user["email"]) and re.match(r'^[a-zA-Z0-9_]+$', user["jmeno"])):
            raise ValueError("Neplatný vstup")
        sql += f"INSERT INTO uzivatel (email, jmeno) VALUES ('{user['email']}', '{user['jmeno']}');\n"
    return sql
