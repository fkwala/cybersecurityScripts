from Crypto.Hash import SHA1

g = 0x56da326ccf7ae2ae34800edc38ca879327b6e2203980aae4a7c563613a982cf92f4685b59cd79ebea9424891e6c28226d8d5a7ab4ef5c09f1d44a28a06d1a9bf0adc4eb6f20b753e1c8d05ddc17ef2fb544e1d5f0bc81fd211eab1970a801342bd2f3870c1580733974e181f45f45f37ee49c73434273900ac7b911cd67e29ce
p = 0x965d3fad0c140e04f422199eed7530a4f50b82e33f937bc2db0ab5deee76692c5c81339e20ac75cc99ca37c8d9cf1ee6505f8fd00c1481ab756a1b505b730dd6a88f921d130ab4d0338a3ce6100f0f24fef52148a177892b5d9b4ebc80e854e82ec86e3b7c45eebe014a285a3ce461899e8ff05e4a17185c4fae59087b66fbad
q = 0xd23e892b6f6cf0c91e21c6b788b8ee81736fba79 
y = 0x2fe5a9715848745ae68eb6658155acea5bd5e4842c4fbc76ea9b21354dd4c52b918ed95c2f07f243c11b5ca80e274432e0d76bf7a57a394d5f32c4c35da8003a5e9cf888f0873fce27105d3cfcc1c4dac8a8e94e5e1eaa6500ebd5eede5f94f3456f0fe530e4d396bd1c7fa23bb06d820a265fc9bbfa4d41a0e697834b9b001f
k = 0xc431208a07dd484674c9da79c2dff66eb7b035d9
r = 0x482d88a9923913ec0cb5401ffd7de9ae7be0016e
s = 0x4e52419f8ae0f230decdb2f5832c5ae0791c4d02

trueFlag = "flag{this_is_an_example}"
trueM = trueFlag.encode()
trueH = int(SHA1.new(trueM).hexdigest(), 16)

x = (s*k-trueH) * pow(r,-1,q) % q

newK = 0xc431208a07dd484674c9da79c2dff66eb7b03512
fakeFlag = "This is a fake flag generated by Felicia."
fakeM = fakeFlag.encode()
fakeH = int(SHA1.new(fakeM).hexdigest(), 16)
fakeR = pow(g, newK, p) % q
fakeS = (pow(newK, -1, q)*(fakeH + x*fakeR)) % q

print(fakeR) # 140719531461964115162925344769470781686117990475
print(fakeS) # 330476141915067267560022386012705196642821149110

