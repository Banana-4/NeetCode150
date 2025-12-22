class TimeMap:
    class Drawer:
        def __init__(self):
            self.timestamps = []
            self.values = []

    def __init__(self):
        self.drawers = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.drawers:
            drawer = self.drawers[key]
            if drawer.timestamps[-1] < timestamp:
                drawer.timestamps.append(timestamp)
                drawer.values.append(value)
        else:
            drawer = self.Drawer()
            drawer.timestamps.append(timestamp)
            drawer.values.append(value)
            self.drawers[key] = drawer

    def get(self, key: str, timestamp: int) -> str:
        if key in self.drawers:
            drawer = self.drawers[key]
            index = self._search_timestamps(drawer.timestamps, timestamp)
            if index != -1:
                return drawer.values[index]
        return ""

    def _search_timestamps(self, stamps: List[int], target: int) -> int:
        start = 0
        end = len(stamps) - 1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if stamps[mid] == target:
                return mid
            if stamps[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if target < stamps[mid]:
            mid -= 1
        return mid
