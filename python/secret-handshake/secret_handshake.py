def commands(binary_str):
    bin = list(binary_str)
    handshake = []

    if bin.pop() == "1":
        handshake.append("wink")

    if bin.pop() == "1":
        handshake.append("double blink")

    if bin.pop() == "1":
        handshake.append("close your eyes")

    if bin.pop() == "1":
        handshake.append("jump")

    if bin.pop() == "1":
        handshake.reverse()

    return handshake
