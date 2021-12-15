s = "X_DSPAM-Confidence:0.8475"
index = s.find(":")
value = float(s[index + 1:])
print(value)
