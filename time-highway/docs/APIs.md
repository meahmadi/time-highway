TimeHighway-API
=========
API endpoints are:

## Auth API
Requests for authentication

#### POST /users/signup
- Email
- Password

Returns:

On success:

    200 {'success': True, 'err': '', 'data': {'profile': {}, 'categories': [cats]}}

On duplicate email:

    200 {'success': False, 'err': 'Email already exists.', 'data': {}}

#### POST /users/login
Parameters:
- Email
- Password

Returns:

On success:

    200 {'success': True, 'err': '', 'data': {'profile': {}}}

On wrong pass:

    200 {'success': False, 'err': 'Password is wrong.', 'data': {}}

On user not found:

    404

#### POST /users/logout
