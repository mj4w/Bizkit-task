from flask import Blueprint, request
from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    results = []
    
    for user in USERS:
        # breakpoint()
        print(user['occupation'])
       
        if 'id' in args and args['id'] and user['id'] == args['id']:
            if user not in results:
                results.append(user)
        elif 'occupation' in args and args['occupation'] and args['occupation'] in user['occupation']:
            if user not in results:
                results.append(user)
        elif 'name' in args and args['name'] and args['name'].lower() in user['name'].lower():
            if user not in results:
                results.append(user)
        elif 'age' in args and args['age']:
            try:
                user_age = int(user['age'])
                search_age = int(args['age'])
                if user_age >= search_age - 1 and user_age <= search_age + 1:
                    if user not in results:
                        results.append(user)
            except ValueError:
                pass
    return results
