def chuck_norris_decode(encoded_message):
    parts = encoded_message.split()
    binary_message = ''
    i = 0
    while i < len(parts):
        prefix = parts[i]
        zero_block = parts[i + 1]
        if prefix == '0':
            binary_message += '1' * len(zero_block)
        elif prefix == '00':
            binary_message += '0' * len(zero_block)
        i += 2
    
    chars = [binary_message[j:j + 7] for j in range(0, len(binary_message), 7)]
    return ''.join([chr(int(c, 2)) for c in chars])