import hashlib

nonce = '416bf668-2518-47eb-856b-4dde4609eeec'
realm = 'https://test.code-kenya.com'
password = 'Paul@40781998'
username    =   str("paulndambo")
requesturi  =   str("https://test.code-kenya.com")
print("username: " + username)
print("nonce: " + nonce)
print("realm: " + realm)
print("password: " + password)
print("\n")

HA1str = username + ":" + realm + ":" + password
HA1enc = (hashlib.md5(HA1str.encode()).hexdigest())
print ("HA1 String: " + HA1str)
print ("HA1 Encrypted: " + HA1enc)
HA2str = "REGISTER:" + requesturi
HA2enc = (hashlib.md5(HA2str.encode()).hexdigest())

print ("HA2 String: " + HA2str)
print ("HA2 Encrypted: " + HA2enc)

responsestr = HA1enc + ":" + nonce + ":" + HA2enc
print("Response String: " + responsestr)
responseenc = str((hashlib.md5(responsestr.encode()).hexdigest()))
print("Response Encrypted" + responseenc)
