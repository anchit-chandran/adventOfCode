i = "nppdvjthqldpwncqszvftbrmjlhg"
start_ix = 0
end_ix = 1
while True:

    if end_ix == len(i)-1:
        break

    start_val = i[start_ix]
    end_val = i[end_ix]

    #check end != start
    if end_val != start_val:
        print(f"{i[:start_ix]}*{start_val}*{i[start_ix+1:end_ix]}~{i[end_ix]}~{i[end_ix+1:]}")
        start_ix+=1
        end_ix+=1
    else:
        break