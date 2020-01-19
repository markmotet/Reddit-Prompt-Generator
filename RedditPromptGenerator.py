import praw
import string

reddit = praw.Reddit(client_id ='CLIENT_ID',
                     client_secret ='CLIENT_SECRET',
                     user_agent ='PROJECT_TITLE_BY_ME',
                     username = 'USERNAME',
                     password = 'PASSWORD')

subreddit = reddit.subreddit('WritingPrompts')

for post in subreddit.top('all', limit=15):
    the_title = post.title

    # Remove the post flair
    if the_title[:4] == "[WP]":
        the_title = the_title[4:]
        the_title = the_title.strip()
        the_title_copy = the_title

        # If the post title has a period and the period is not at the end of the sentence, cut the title after the first sentence and four words
        if the_title_copy.find('.') != -1 and the_title_copy.find('.') + 1 != len(the_title_copy):

            # Everything after the first sentence
            the_title_copy = the_title_copy[the_title_copy.find('.') + 2:]

            # Append the following four words after the first sentence to the first sentence
            if len(the_title_copy.split()) >= 4:
                start_of_sentence = ' ' + the_title_copy.split()[0] + ' ' + the_title_copy.split()[1] + ' ' + the_title_copy.split()[2] + ' ' + the_title_copy.split()[3]
                the_title = the_title[:the_title.find('.') + 1]
                the_title = the_title + start_of_sentence

        # If the post title is one sentence, remove the last two words
        else:
            the_title = the_title.split()
            the_title.pop()
            the_title.pop()
            the_title = ' '.join(the_title)
        
        print(the_title)