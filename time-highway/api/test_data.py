import random
from settings import *
from mongoengine import *
from faker import Faker
from models import UserModel, StoryModel

connect('timehighway', host=MONGO_HOST, port=MONGO_PORT,
        username=MONGO_USERNAME, password=MONGO_PASSWORD)


fake = Faker()
USER_NUMBERS = 100
STORY_NUMBERS = 1000
STORIES = [
	StoryModel(
		name="story_num%d" % i,
		desc=fake.text(),
	).save() for i in range(STORY_NUMBERS)
]

def fake_user():
	for i in range(USER_NUMBERS):
		u = UserModel(
			firstname=fake.first_name(),
			lastname=fake.last_name(),
			email=fake.email(),
			password="ABCD"*4,
		)
		u.stories = [random.choice(STORIES) for i in range(random.randint(1, 4))]
		u.save()

if __name__ == '__main__':
	fake_user()