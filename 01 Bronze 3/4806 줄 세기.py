def main():
    cnt = 0
    while 1:
        try:
            string = input()
            cnt += 1
        except:
            print(cnt)
            break

if __name__=='__main__':
    main()
