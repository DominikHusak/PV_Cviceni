def build_sql_select_all_from_table(table_name):
    return "SELECT * FROM {}".format(table_name)

def build_sql_select_custom_from_users(columns):
    placeholders = ', '.join(columns)
    sql = "SELECT {} FROM USER".format(placeholders)
    return sql

def build_sql_select_users_order_by_custom(order_by_section):
    return "SELECT * FROM USER ORDER BY {}".format(order_by_section)

