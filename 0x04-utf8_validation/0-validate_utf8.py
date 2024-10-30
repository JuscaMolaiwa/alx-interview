def validUTF8(data):
    """Determines if the given data set is a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for UTF-8 byte types
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Mask to get only the last 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes for the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # 1-byte character (0xxxxxxx)
                return False
        else:
            # Check if the byte is a continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0
