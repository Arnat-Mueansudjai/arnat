def encrypt(message,key):
    encrypted = ""
    for char in message:
        #เช็คตัวพิมพ์ใหญ่
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A')) 
            # ord(char) - ord('A') ทำให้ A = 0 และไปบวก key เพื่อหาตัวถัดไป % 26 เพราะเอามาหมุนหา A-Z และมาบวก ord('A') เพื่อทำให้กลายเป็นเลขแอสกีเหมือนดิม
            # และสุดท้ายแปลงกลับมาเป็น chrเช็คพิมพ์เล็ก
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        # ถ้าไม่ใช่ตัวอักษร (space, punctuation) เก็บไว้เหมือนเดิม
        else:
            encrypted += char
    return encrypted
message = input("Enter the message to encrypt: ")
key = int(input("Enter the key (number): "))

encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
