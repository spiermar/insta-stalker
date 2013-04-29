import calendar
import urlparse
from datetime import datetime
from instagram.client import InstagramAPI
from instagram.helper import datetime_to_timestamp

access_token = '32950274.29308ad.e5b10814e6dc4d69a78279c4277921ef'
api = InstagramAPI(access_token=access_token)

tag_name = 'encorebeachclub'
count = 20
# max_id = datetime_to_timestamp(datetime.now())
max_id = 1349395199000

for i in range(2):

	recent_media, next = api.tag_recent_media(count, max_id, tag_name)

	print 'count: ' + str(len(recent_media))

	for media in recent_media:
		print 'username: ' + media.user.username
		print 'link: ' + media.link
		print 'time: ' + str(media.created_time) + ' (' + str(datetime_to_timestamp(media.created_time)) + ')'
		print 'id: ' + media.id
		print 'url: ' + media.images['standard_resolution'].url

	parsednext = urlparse.urlparse(next)

	max_id = urlparse.parse_qs(parsednext.query)['max_tag_id'][0]

	print 'max_tag_id: ' + max_id