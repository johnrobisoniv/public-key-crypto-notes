# verified data integrity
# If we want to communicate privately over public networks, and
# both want to be sure that the other sent the message, and that
# the message hadn't been changed or corrupted


# First, import packages
import publickeycryptomodule as pkcm                # the module object**

# I made this up. This is a simplified explanation. 
# Hope to update with actual libraries and methods etc



# pkcm has the following methods:

pkcm.encrypt(public_key, unencrypted_data):
    # process by complicated algorithm that encrypts unencrypted data
    return encrypted_data


pkcm.decrypt(private_key, encrypted_data):
    # another complex algorithm
    return decrypted_data
    # ( note ! : decrypted_data == unencrypted_data )

pkcm.hash(data):
    return data_hash

pkcm.sign(private_key, unsigned_data):
    # this is called an abstraction, where we don't dive into exactly how this
    # complex algorithm works
    return signed_data


pkcm.verify(public_key, signed_data):
    # ... you get the idea
    return designed_data # lol get it - like unencrypt / decrypt? :P
    # ( again, unsigned_data == designed_data )


                                                    # ** including
                                                    # encryption, decryption,
                                                    # hashing and signing algorithms,
                                                    # that are called methods, or
                                                    # functions accessible to
                                                    # an object
                                                    # now the variable RSA equals
                                                    # RSA = Crypto.PublicKey

                                                    # Methods and instance variables
                                                    # are accessible to the object
                                                    # by concatenating the next
                                                    # level down's key, thereby
                                                    # accessing its corresponding
                                                    # value. i.e to access the
                                                    # RSA




# Then, define functions
# Let's assume that players already have their keypairs generated ...

kuzis_public_key = 'atonofrandomletters'
kuzis_private_key = 'even more random letters or w/e'
    # in the true use case you would be processing these algorithms on your
    # local device - this should be the **only** time your public key is
    # exposed in an unencrypted form.



johns_public_key = # yah - you already have it
johns_private_key = # no way

# ... and let's also assume that you have sent your public key to me, and I mine to you




# First, let's say you want to send me a message.

## this takes place on Kuzi's local machine
# first, the message is input
# and the string of characters is assigned
# to a variable:

kuzis_msg = 'Hi. I\'m Kuzi, I\'m a cool guy.'                                       # see how i escaped characters  that would have ended the string - a single quotation mark ... with a forward slash \ ?


# then, we pass the message and the recipient's public key into the pkcm.encrypt() method call
kuzis_encrypted_msg = pkcm.encrypt(johns_public_key, kuzis_msg)

# since the method (a type of function) call returns a string of bits encoding characters,
# the kuzis_encrypted_msg variable now points to an encrypted message.
print kuzis_encrypted_msg
# see?



# Now that this is encrypted in a way that only I can decrypt (since only I
# have the corresponding private key) you can confidently transmit this over
# the airwaves (where anyone can read the information)

# So let's say you transmit that message to my phone:

# [======]
# |      |
# | kuzis|
# | phone|
# [======]
#    ||
#    ||
#    ||
#    ||
#    ||
#     \\
#      \\
#       \\
#        \\
#         \\
#          \\
#         [======]
#         |      |
#         | johns|
#         | phone|
#         [======]

# (note this is an entirely new instance of the same program running on a distant
# device, possibly only connected wirelessly)
# and the app receives kuzi_encrypted_msg
kuzis_received_msg = 'randomlookingletters'

# Here I do have a variable set to my private key
iv_private_key = 'yeahrightillshowyouthislol'


kuzis_decrypted_msg = pkcm.decrypt(iv_private_key, kuzis_received_msg)
print kuzis_decrypted_msg
    # 'Hi. I\'m Kuzi, I\'m a cool guy.'


#  EVERYTHING BELOW HERE IS NOTES - DISREGARD UNLESS YOU WANT TO GET CONFUSED
# vvvvvvvvvvVvvvvvvvvvvVvvvvvvvvvvVvvvvvvvvvvVvvvvvvvvvvVvvvvvvvvvvVvvvvvvvvvv

# Cool. I got a private message from you and figured out what you said.
# But how do I know this was from you? And how do I know that what you said
# was what you meant to say?

# Enter the ability to cryptographically sign data.


# So I want to send you a message, and I want you to be sure that it was from
# me and hadn't been changed en route ...
# We will eventually want to transmit a python dictionary (or, similarly in javascript, an object literal  )
# that looks like this:
# msg = {
#     'iv_signature': '',
#     'iv_encrypted_msg': '',
# }
#

# iv_msg = 'and my name\'s John - I\'m not nearly \
#         as cool.'
#
# iv_msg_hash = pkcm.hash(iv_msg)
# iv_signed_msg = pkcm.sign()
#
# msg_to_sign = {
#     'hash': iv_msg_hash,
#     'encrypted_msg':
# }
#
#
#
#
#
# iv_encrypted_msg = pkcm.decrypt()
#
#
#     unsigned_hash = pkcm.hash(unsigned_data)
#
# x.
