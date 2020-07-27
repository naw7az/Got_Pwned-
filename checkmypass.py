import requests
import hashlib  # to hash our password
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:  # we only need response 200
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    # this function was defined after pwned_api_check function to use in it.
    hashes = (line.split(':') for line in hashes.text.splitlines())  # read about splitlines(), why is it needed
    for h, count in hashes:  # h is tail hashes of all password with same first5_char, count is time it got hacked
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    # checking password exists in API response or not
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5_char)
    print(response)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should probably change it>')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'

if __name__ == "__main__":  
    sys.exit(main(sys.argv[1:]))  # we will get done! at the end because we exiting from the main function.
    

# this part is just to show how we got sha1pass in pwned_api_check function:
# def pass_to_hash_steps(secret):
#     print(secret)
#     print(secret.encode('utf-8'))  # this is needed to convert into hash
#     print(hashlib.sha1(secret.encode('utf-8')))  # converted to hash object
#     print(hashlib.sha1(secret.encode('utf-8')).hexdigest())  # using hexdigest method to get hash code(hexadecimal)
#     print(hashlib.sha1(secret.encode('utf-8')).hexdigest().upper())  # need hash code in caps
# pass_to_hash_steps('123')
