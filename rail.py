def rail_fence_encrypt(plain_text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in plain_text:
        fence[rail].append(char)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
    
    encrypted_text = ''.join(char for rail in fence for char in rail)
    return encrypted_text

def rail_fence_decrypt(encrypted_text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    for char in encrypted_text:
        fence[rail].append(None)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
            
    index = 0
    for _ in range(rails):
        for j in range(len(encrypted_text)):
            if index < len(encrypted_text):
                fence[_][j] = encrypted_text[index]
                index += 1
            
            if len(fence[_]) == j + 1 or len(fence[_]) == 1:
                break
    
    rail = 0
    direction = 1
    decrypted_text = ''
    for _ in range(len(encrypted_text)):
        decrypted_text += fence[rail].pop(0)
        rail += direction
        
        if rail == rails - 1 or rail == 0:
            direction = -direction
            
    return decrypted_text

# Example usage:
plain_text = "Hello, World!"
rails = 3
encrypted_text = rail_fence_encrypt(plain_text, rails)
print("Encrypted:", encrypted_text)

decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print("Decrypted:", decrypted_text)
