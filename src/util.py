import hashlib

def crypt_password(password):
    encoded_password = password.encode()
    password_sha3 = hashlib.sha3_256(encoded_password)
    return password_sha3.hexdigest()


def raise_error(msg_sys, msg_error, status_error):
    return{
        'msg_error' :  msg_error,
        'msg_sys' :  msg_sys,
        'status_error' :  status_error
    }
