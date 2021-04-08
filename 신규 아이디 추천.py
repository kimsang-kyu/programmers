def solution(new_id):
    #1
    new_id = new_id.lower()
    
    #2
    new_id2 = ''
    for id in new_id:
        if id.isalpha() or id.isdigit() or id in ['-', '_','.']:
            new_id2+=id
        
    #3
    while '..' in new_id2:
        new_id2 = new_id2.replace('..', '.')
    
    #4
    new_id = new_id2.strip(".")
    
    #5
    if len(new_id) == 0:
        new_id = new_id.replace("",'a')
    
    #6
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.strip(".")
    else:
        new_id = new_id
        
    #7
    if len(new_id) <= 2:
        while True:
            new_id = new_id + new_id[-1]
            if len(new_id) >= 3:
                break
        
    return new_id
