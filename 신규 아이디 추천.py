def solution(new_id):
    #1
    new_id = new_id.lower()
    
    #2
    new_id2 = ''
    for id in new_id:
        if id.isalpha() or id.isdigit() or id in ['-', '_','.']:
            new_id2+=id
        
    #3
    new_id3 = new_id2.replace('..',".").replace("..",'.')
    
    #4
    new_id4 = new_id3.strip(".")
    
    #5
    new_id5 = new_id4.replace(" ",'a')
    
    #6
    if len(new_id5) > 16:
        new_id6 = new_id5[:15]
    else:
        new_id6 = new_id5
        
    #7
    if len(new_id6) <= 2:
        while True:
            new_id6 = new_id6 + new_id6[-1]
            if len(new_id6) >= 3:
                break
        
    return new_id6
