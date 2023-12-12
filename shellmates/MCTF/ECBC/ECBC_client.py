from pwn import *

def main():
    host = "0.0.0.0"  # Update with the server's IP if necessary
    port = 1337

    conn = remote(host, port)

    while True:
        menu = conn.recv().decode()
        print(menu)

        choice = input("Enter your choice (1/2/3): ")
        conn.send(choice.encode())

        if choice == '1':
            encrypted_flag = conn.recv().decode()
            print(encrypted_flag)
        elif choice == '2':
            ciphertext_prompt = conn.recv().decode()
            print(ciphertext_prompt, end="")
            ciphertext = input()
            conn.send(ciphertext.encode())
            decrypted_flag = conn.recv().decode()
            print(decrypted_flag)
        elif choice == '3':
            conn.close()
            break

if __name__ == "__main__":
    main()
