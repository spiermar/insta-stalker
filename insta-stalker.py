import calendar
import urlparse
import ConfigParser
from datetime import datetime
from instagram.client import InstagramAPI
from instagram.helper import datetime_to_timestamp
from instagram.helper import timestamp_to_datetime

config = ConfigParser.ConfigParser()
config.read('insta-stalker.cfg')

access_token = config.get('insta-stalker', 'access_token')

api = InstagramAPI(access_token=access_token)

tag_name = 'encorebeachclub'
from_time = 1348876800000
to_time = 1349395200000
count = 20

print 'from_time: ' + str(timestamp_to_datetime(from_time / 1000))
print 'to_time: ' + str(timestamp_to_datetime(to_time / 1000))

max_id = to_time
while (max_id > from_time):

	recent_media, next = api.tag_recent_media(count, max_id, tag_name)

	# print 'count: ' + str(len(recent_media))

	for media in recent_media:
		# print 'username: ' + media.user.username
		# print 'link: ' + media.link
		print 'time: ' + str(media.created_time)
		# print 'id: ' + media.id
		# print 'url: ' + media.images['standard_resolution'].url

	parsednext = urlparse.urlparse(next)

	max_id = int(urlparse.parse_qs(parsednext.query)['max_tag_id'][0])

	print 'max_tag_id: ' + str(max_id) + ' (' + str(timestamp_to_datetime(max_id / 1000)) + ')'