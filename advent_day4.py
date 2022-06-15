import hashlib


# part 1
def hash(answer : int) -> str:
    while True:
        key = "yzbqklnj" 
        key = (key + str(answer))
        encoded_key = hashlib.md5(key.encode())
        hashed_key = (encoded_key.hexdigest())

        if hashed_key[:5] == "00000":
            return answer

        answer += 1
    
    
def main() -> None:
    print(hash(0))


if __name__ == "__main__":
    main()