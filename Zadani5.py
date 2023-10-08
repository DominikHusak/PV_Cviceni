def build_sql_update_email_by_id(email, user_id):
    return "UPDATE uzivatel SET email='{}' WHERE id={}".format(email, user_id)

def build_sql_delete_all_by_table(table_name):
    return "DELETE FROM {}".format(table_name)

def build_sql_update_users(users):
    sql = ""
    for user in users:
        sql += "UPDATE uzivatel SET email='{}', jmeno='{}' WHERE id={};".format(user["email"], user["jmeno"], user["id"])
    return sql