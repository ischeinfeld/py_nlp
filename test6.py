from decoder_class_log import Decoder

sentence = "Dr. Scheinfeld saw thrity two patients today."

decoder = Decoder("train", 5)

decode = decoder.decode(sentence)

print(list(zip(decode[0],decode[1])))
