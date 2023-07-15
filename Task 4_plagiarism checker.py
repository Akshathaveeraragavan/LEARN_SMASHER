from difflib import SequenceMatcher #import sequencematcher module
text1=input('Enter text1')      #get the input of the text 
text2=input('Enter text2')
match=SequenceMatcher(None,text1,text2)   #check for the plagiarism
ans=match.ratio()*100            # convert the ratio 
print(int(ans),'% is a plagiarized content')
