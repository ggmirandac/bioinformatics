def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 
print(PatternCount("CGCG","CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"),"AAAAA")
max_coso=0
max_text=""
for cant in range(len("GATCCAGATCCCCATAC")):
    #print(len("GATCCAGATCCCCATAC"))
    #print(cant)
    if cant+2<len("GATCCAGATCCCCATAC"):
        texto="GATCCAGATCCCCATAC"[cant:cant+2]
        canti=PatternCount("GATCCAGATCCCCATAC",texto)
    #    print(texto)
        if canti>max_coso:
            max_coso=canti
            max_text=texto
print(max_text)
print(max_coso)