import uuid
from typing import Generator


class URLs:
    URLS = [
        "https://main.node.com",
        "https://helper.node.com",
        "http://private.node.com",
        "https://public.node.com",
    ]

    @staticmethod
    def set() -> Generator:
        while True:
            for url in URLs.URLS:
                yield url

    @staticmethod
    def update(url: Generator) -> str:
        return next(url)


def parser():
    generator = URLs.set()
    print(f"START! URL: {next(generator)}")
    keys = [uuid.uuid4() for i in range(50)]
    for index, secret_key in enumerate(keys):
        try:
            if index in [5, 15, 35, 50]:
                raise Exception("This index is so bad!")
        except Exception as error:
            print(f"ERROR: {error}")
            print(f"UPDATE! NEW URL: {next(generator)}")
    return True


if __name__ == '__main__':
    print(parser())
