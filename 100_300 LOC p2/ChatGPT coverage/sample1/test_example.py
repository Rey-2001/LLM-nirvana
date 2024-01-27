
import asyncio
import pytest
from decorators import cached_property

class TestCachedProperty:
    def test_cached_property(self):
        class MyClass:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        assert obj.y == 6

    @pytest.mark.asyncio
    async def test_cached_property_async(self):
        class MyClass:
            def __init__(self):
                self.x = 5

            @cached_property
            async def y(self):
                await asyncio.sleep(1)  # simulate async operation
                return self.x + 1

        obj = MyClass()
        assert await obj.y == 6

    def test_cached_property_multiple_instances(self):
        class MyClass:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj1 = MyClass()
        obj2 = MyClass()

        assert obj1.y == 6
        obj2.x = 10
        assert obj2.y == 11
        assert obj1.y == 6

    def test_cached_property_reset(self):
        class MyClass:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        assert obj.y == 6
        obj.x = 10
        assert obj.y == 11

        del obj.y
        assert obj.y == 11

    def test_cached_property_no_overwrite(self):
        class MyClass:
            def __init__(self):
                self.x = 5
                self.y = 10

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        assert obj.y == 10
