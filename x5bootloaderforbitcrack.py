import subprocess
import secrets

def generate_random_hex():
    start_hex = int('20000000000000000', 16)
    end_hex = int('3ffffffffffffffff', 16)
    random_hex = hex(secrets.randbelow(end_hex - start_hex + 1) + start_hex)[2:].zfill(16)
    return random_hex

def start_cubitcrack(hex_keyspace):
    command = f'cuBitCrack.exe -i  ***incert text for addresses*** -c -u -b 64 -t 512 -p 128 --stride 1 --keyspace {hex_keyspace}'
    subprocess.Popen(command, cwd=r' ***incert file loacion***      ', shell=True)

if __name__ == '__main__':
    num_instances = 5

    for _ in range(num_instances):
        random_hex = generate_random_hex()
        start_cubitcrack(random_hex)
