def main():
    arr = {10,25.5,"Hey"}
    print(type(arr))
    print(len(arr))

    print(arr)

    for value in arr:
        print(value)

    if "Hey" in arr:
        print("Hey is there")

        arr.add(20)
        print(arr)

        #arr.remove(20)
        #print(arr)

        arr.discard(120)
        print(arr)

if __name__=="__main__":
    main()