f = open("test.txt", "w")  # opens file with name of "test.txt"
for x in range(81):    # for every pixel:
    f.write("\n")
    for y in range(49):
        f.write("I am a test file.")
        f.write("Maybe someday, he will promote me to a real file.")
        f.write("Man, I long to be a real file")
        f.write("and hang out with all my new real file friends.")
f.close()
