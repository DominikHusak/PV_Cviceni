def build_sql_select_user_by_username_and_variable_symbol(username, vs):
    return "SELECT * FROM USER WHERE USERNAME=%s AND VARIABLE_SYMBOL=%s"

def build_sql_select_user_by_id(user_id):
    return "SELECT * FROM USER WHERE ID=%s"

def build_sql_select_users_order_by_custom(order_by_section):
    return "SELECT * FROM USER ORDER BY {}".format(order_by_section)