from decoder_class_log import Decoder

sentence = "The bill, whose backers include Chairman Dan Rostenkowski -LRB- D., Ill. -RRB-, would prevent the Resolution Trust Corp. from  raising temporary working capital by  having an RTC-owned bank or thrift issue debt that  would n't beB counted on the federal budget."

decoder = Decoder("train", 5)

decode = decoder.decode(sentence)

print(list(zip(decode[0],decode[1])))
