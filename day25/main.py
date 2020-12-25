def transform(subject_number, target_number, max_loop_size):
    value = subject_number
    loop_size = 0
    while loop_size <= max_loop_size:
        value = value * subject_number
        value = value % 20201227
        if value == target_number:
            print("{} {}".format(loop_size, value))
            return loop_size
        loop_size +=1
    return value

def run():
    card_pub_key = 15335876
    door_pub_key = 15086442
    card_loop_size = transform(7,card_pub_key,100000000)
    door_loop_size = transform(7,door_pub_key, 100000000 )
    card_encryption_key = transform(door_pub_key, 0, card_loop_size)
    door_encryption_key = transform(card_pub_key, 0, door_loop_size)
    print("{} {}".format(card_encryption_key, door_encryption_key))


if __name__ == '__main__':
    run()