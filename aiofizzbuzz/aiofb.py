class AioFizzBuzz:

    def __init__(self, start: int, end: int = None, step=1):
        if end is None:
            self.start = 0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = 1

    @staticmethod
    async def fb(i: int):
        return "fizzbuzz"[i**4 % 3 * 4:9 - i**8 % 5 * 5] or str(i)

    async def __aiter__(self):
        while self.start < self.end:
            yield await self.fb(self.start)
            self.start += self.step
