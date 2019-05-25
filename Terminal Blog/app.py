_author_ = 'Ta-Seen Junaid'

from models.post import Post
from database import Database

Database.initialize()

post = Post(blog_id="123",
            title="Another great great post",
            content="This is some sample content ..........xxxxxxxxxxxxxx........",
            author="Tas")

post.save_to_mongo()
