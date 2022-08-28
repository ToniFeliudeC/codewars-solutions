

#My solution

def amount_of_pages(summary):
    
    page = 1
    digits = 0
    
    while digits < summary:
        digits += len(str(page))
        page += 1
    
    return page - 1