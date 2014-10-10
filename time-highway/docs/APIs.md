Time-Highway-API
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


## User Data API

#### GET /user/stories

Parameters:

Returns:

On success:
	
	200, {'data': {
			'stories': [(<story_id>)*]
		}
	}

On error:
	
	404

#### POST /story

For change an story events 
Parameters:
- story_id (type: id)
- events (type: list of ids)

Returns:

On success:
	
	200, {'success': True} 

On wrong story_id:
	
	404, {'err': 'Story not found.'}

On wrong each event_id:

	404, {'err': 'Event not found.'}

On permission error:

	403, {'err': 'You do not have access.'}

On error while saving:

	404, {'err': 'Error while saving.'}