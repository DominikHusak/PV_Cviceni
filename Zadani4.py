def build_sql_update_user_jmeno_by_id(name, user_id):
    return "UPDATE uzivatel SET jmeno=%s WHERE id=%s"

def build_sql_delete_by_table_and_id(table_name, user_id):
    return "DELETE FROM {} WHERE id=%s".format(table_name)

def build_sql_insert_users(users):
    sql = ""
    for user in users:
        sql += "INSERT INTO uzivatel (email, jmeno) VALUES (%s, %s);"
    return sql