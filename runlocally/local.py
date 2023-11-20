import subprocess
import time
import sys

import minio_screens
import redis_seed


def run_docker_compose(composition: str) -> bool:
    try:
        subprocess.check_call([
            "docker-compose",
            "-f",
            composition + "/docker-compose.yml",
            "-p",
            composition,
            "up",
            "-d"
        ])
        return True
    except:
       return False

def main():
    redis_ok = run_docker_compose("redis")
    minio_ok = run_docker_compose("minio")
    if not redis_ok:
        print("Something wrong with Redis")
    if not minio_ok:
        print("Something wrong with Minio")

    time.sleep(3)

    if not "--no-redis-seed" in sys.argv:
        redis_seed.redis_main()

    if not "--no-minio-screens" in sys.argv:
        minio_screens.minio_main()

main()