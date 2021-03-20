ps = ["hello\n"]*1000

with open("generator.txt", 'w') as f:
    for p in ps:
        f.write(p)

