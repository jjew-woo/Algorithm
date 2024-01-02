import re
from collections import defaultdict

def solution(word, pages):
    urls = []
    links = defaultdict(set)
    page_info = {}
    
    word = word.lower()
    for page in pages:
        url = ''
        p = re.compile("<meta property=\"og:url\" content=\"https://\S+")
        for l in p.findall(page):
            url = l[33:-3]
        urls.append(url)
        
        p = re.compile("<a href=\"https://\S+\"")
        link = p.findall(page)
        for l in link:
            links[l[9:-1]].add(url)
        
        tokens = re.sub('[^a-zA-Z]',' ',page).split()
        count = 0
        for token in tokens:
            if word == token.lower(): count+=1
        
        page_info[url] = [count, len(link)]
    
    answer = 0; max_score = 0
    for i in range(len(urls)):
        url = urls[i]
        score = page_info[url][0]
        for link in links[url]:
            score += page_info[link][0]/page_info[link][1]
        
        if max_score < score:
            answer = i
            max_score = score
            
    return answer