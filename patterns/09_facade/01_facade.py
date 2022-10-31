class Buffer:
    def __init__(self, width: int = 30, height: int = 20) -> None:
        self.height = height
        self.width = width
        self.buffer = [" "] * (width * height)

    def __getitem__(self, item) -> str:
        return self.buffer.__getitem__(item)

    def write(self, text: str) -> None:
        self.buffer += text


class Viewport:
    def __init__(self, buffer: Buffer = Buffer()) -> None:
        self.buffer = buffer
        self.offset = 0

    def get_char_at(self, index: int) -> str:
        return self.buffer[index + self.offset]

    def append(self, text: str) -> None:
        self.buffer.write(text)


class Console:
    def __init__(self) -> None:
        b = Buffer()
        self.current_viewport = Viewport(b)
        self.buffers = [
            b,
        ]
        self.viewports = [
            self.current_viewport,
        ]

    def write(self, text: str) -> None:
        self.current_viewport.append(text)

    def get_char_at(self, index: int) -> str:
        return self.current_viewport.get_char_at(index)


if __name__ == "__main__":
    c = Console()
    c.write("check")
    ch = c.get_char_at(0)
    print(ch)
