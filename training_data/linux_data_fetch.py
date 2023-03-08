import praw

reddit = praw.Reddit(
	client_id='',
	client_secret='',
	user_agent=''
)

subreddits = ['linux', 'linuxmasterrace']

with open('training_data.txt','w', encoding='utf-8') as f:
	for subreddit in subreddits:
		index = 0
		for submission in reddit.subreddit(subreddit).top(limit=1000):
			index += 1		
			if submission.is_self:
				f.write(submission.selftext + '\n')
				for comment in submission.comments:
					if hasattr(comment, "body"):
						f.write(comment.body + '\n')
						print('GOT COMMENT')
				print(subreddit)
				print(index)
