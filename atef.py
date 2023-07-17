def create_youtube_video(title, description):
	youtube_video = {"title" : title, "description" : description, "likes" : 0,"dislike" : 0,"comments" : {} }
	return  youtube_video


def like(dicionary):
	if "likes" in dicionary:
		dicionary["likes"] = dicionary["likes"]+1
		return dicionary

def dislike(dicionary):
	if "dislike" in dicionary:
		dicionary["dislike"] = dicionary["dislike"]+1
		return dicionary

def comment(dicionary):
	usrname = input("Enter your name: ")
	comment = input("Enter your comment: ")
	dicionary["comments"][usrname]=comment



x = create_youtube_video("Atef","gsyghsgdhsgh")
print(x)
like(x)
print(x)
dislike(x)
print(x)
print(x)
comment(x)
comment(x)
print(x)

     

