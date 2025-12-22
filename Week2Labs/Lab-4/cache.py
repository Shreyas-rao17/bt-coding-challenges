class Cache:
    _MAX_CAPACITY = 0

    """
    Static method to get the maximum capacity of the cache
    """
    @staticmethod
    def get_max_capacity():
        if( Cache._MAX_CAPACITY == 0):
            Cache._MAX_CAPACITY = int(input("Enter the maximum capacity of the cache: "))
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
