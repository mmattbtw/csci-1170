def falling_distance(time):
    g = 9.8
    return 1/2*g*(time**2)
def main():
    for i in range(1,11):
        print(i, falling_distance(i))
        
main()