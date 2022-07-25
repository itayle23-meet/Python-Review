
def create_youtube_vid(title,description):
	new_vid = {"title" : title , "description" : description , "likes" : 0 , "dislikes" : 0, "comments" : {}}
	return new_vid

def like(new_vid):
    new_vid["likes"] += 1
    return new_vid

def dislike(new_vid):
    new_vid["dislikes"] += 1
    return new_vid

def add_comment(new_vid, username, comment_text):
	new_vid["comments"][username] = comment_text
	return new_vid

new_vid = create_youtube_vid("fun_video" , "this video is fun")
like(new_vid)
dislike(new_vid)
add_comment(new_vid , "user" , "cool!")
print(new_vid)
for i in range (494):
	like(new_vid)
print(new_vid)