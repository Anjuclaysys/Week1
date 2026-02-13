from user_class import CompanyUser


def format_users(users_json:list)->list:
    """
    Docstring for format_users
    
    :param users_json: users data
    :type users_json: list
    :return: needed user details
    :rtype: list
    """

    users =[]
    for user in users_json:
        formatted_user = CompanyUser(
            user_id=user['id'],
            name=user['name'],
            email=user["email"],
            company_name=user['company']['name']
        )

        users.append(formatted_user)

    return users
